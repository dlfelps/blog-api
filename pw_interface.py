from peewee import Model, SqliteDatabase, CharField, IntegerField, ForeignKeyField, DateTimeField
from models import Post as PostDantic
import datetime

db = SqliteDatabase(':memory:', pragmas = {'foreign_keys': 1})
class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    content = CharField(max_length=255)
    category = CharField(max_length=255)
    createdAt = DateTimeField()
    updatedAt = DateTimeField()
    
 

class Tag(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    
class TagPosts(BaseModel):
    post = ForeignKeyField(Post, backref='tags')
    tag = ForeignKeyField(Tag, backref='posts')

## Initialize upon LOAD
db.connect()
db.create_tables([Post, Tag, TagPosts])


def reverse(postT: Post) -> PostDantic:
  # converts PostTable to Post
  # doesn't modify fields
  tag_list = [t.tag.name for t in postT.tags]

  return  PostDantic(id=postT.id,
                    title=postT.title, 
                    content=postT.content,
                    category=postT.category,
                    createdAt=postT.createdAt,
                    updatedAt=postT.updatedAt,
                    tags=tag_list)


def get_or_create(name: str) -> Tag:
    tag, _ = Tag.get_or_create(name=name)
    return tag


def create_record(post: PostDantic) -> PostDantic:
  # convert to Post (and save to db)
  postT = Post.create(title=post.title, 
                content=post.content,
                category=post.category,
                createdAt=post.createdAt,
                updatedAt=post.updatedAt)

  # get or create tags

  tags = list(map(get_or_create, post.tags))

  # add entries to joining table
  for t in tags:
      TagPosts.create(post=postT.id, tag=t.id)

  # convert back to Post (this adds the id, previously unassigned)
  updated_post = reverse(postT)

  return updated_post

def get_record(id: int) -> Post:
    postT = Post.get_by_id(id)
    return reverse(postT)

def update_record(post: Post) -> Post:
    pass

def delete_record(id: int) -> None:
    pass

