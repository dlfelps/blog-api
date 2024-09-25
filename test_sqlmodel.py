from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

# Team -> Post
# Hero -> Tag

class TagPostLink(SQLModel, table=True):
    post_id: int | None = Field(default=None, foreign_key="post.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str

    tags: list["Tag"] = Relationship(back_populates="posts", link_model=TagPostLink)


class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tag: str = Field(index=True)
    
    posts: list["Post"] = Relationship(back_populates="tags", link_model=TagPostLink)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_posts():
    with Session(engine) as session:
      tag_one = Tag(tag="one")
      tag_two = Tag(tag="two")
      
      post_one = Post(
          title="First post",
          content="hello world",
          tags=[tag_one])

      post_two = Post(
        title="Second post",
        content="next",
        tags=[tag_two])

      post_three = Post(
        title="Third post",
        content="last",
        tags=[tag_one, tag_two])
      

      session.add(post_one)
      session.add(post_two)
      session.add(post_three)
      session.commit()

      session.refresh(post_one)
      session.refresh(post_two)
      session.refresh(post_three)        

def select_posts():
    with Session(engine) as session:
        statement = select(Tag).where(Tag.tag == "one")
        result = session.exec(statement)
        tag_one = result.first()
        print(tag_one)

        statement = select(Post).where(Post.tags.contains(tag_one))
        result = session.exec(statement)
        posts = result.all()
        print(posts)


def main():
    create_db_and_tables()
    create_posts()
    select_posts()


if __name__ == "__main__":
    main()