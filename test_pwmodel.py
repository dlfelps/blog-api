from peewee import Model, SqliteDatabase, CharField, IntegerField, ForeignKeyField


db = SqliteDatabase(':memory:', pragmas = {'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db


class Post(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    content = CharField(max_length=255)
 

class Tag(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    
class TagPosts(BaseModel):
    post = ForeignKeyField(Post, backref='tags')
    tag = ForeignKeyField(Tag, backref='posts')



def create_db_and_tables():
    db.connect()
    db.create_tables([Post, Tag, TagPosts])


def create_posts():
    
    tag_one = Tag.create(name="one")
    tag_two = Tag.create(name="two")
    
    post_one = Post.create(title="First post", content="hello world")
    TagPosts.create(post_id=post_one.id, tag_id=tag_one.id)    

    post_two = Post.create(title="Second post", content="next")
    TagPosts.create(post_id=post_two.id, tag_id=tag_two.id)    
    
    post_three = Post.create(title="Third post", content="last")
    TagPosts.create(post_id=post_three.id, tag_id=tag_one.id)
    TagPosts.create(post_id=post_three.id, tag_id=tag_two.id)
      
     

def select_posts():
    
    # find all posts with tag "one"
    tag_one = Tag.get_or_none(Tag.name == "two")
    posts = Post.select().join(TagPosts).where(TagPosts.tag_id == tag_one)
    print([p for p in posts])

    print([p.post for p in tag_one.posts])

def close_db():
    db.close()

def main():
    create_db_and_tables()
    create_posts()
    select_posts()
    close_db()


if __name__ == "__main__":
    main()