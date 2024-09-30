from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from datetime import datetime
from models import Post

# Initialize db upon module load
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

class TagPostLink(SQLModel, table=True):
    post_id: int | None = Field(default=None, foreign_key="post_table.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag_table.id", primary_key=True)


class PostTable(SQLModel, table=True):
    __tablename__ = "post_table"
    id: int | None = Field(default=None, primary_key=True)
    title: str 
    content: str
    category: str
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    tags: list["TagTable"] = Relationship(back_populates="posts", link_model=TagPostLink)


class TagTable(SQLModel, table=True):
    __tablename__ = "tag_table"
    id: int | None = Field(default=None, primary_key=True)
    tag: str = Field(index=True)
    
    posts: list[PostTable] = Relationship(back_populates="tags", link_model=TagPostLink)


def forward(post: Post) -> PostTable:
  # converts Post to PostTable
  # doesnt modify fields (except id on write)
  return  PostTable(title=post.title, 
                    content=post.content,
                    category=post.category,
                    createdAt=post.createdAt,
                    updatedAt=post.updatedAt,
                    tags=list(map(get_or_create_tag, post.tags)))
  

def reverse(postT: PostTable) -> Post:
  # converts PostTable to Post
  # doesn't modify fields
  return  Post(title=postT.title, 
                  content=postT.content,
                  category=postT.category,
                  createdAt=postT.createdAt,
                  updatedAt=postT.updatedAt,
                  tags=list(map(lambda x: x.tag, postT.tags)))


def get_or_create_tag(tag: str) -> TagTable:
  with Session(engine) as session:
    statement = select(TagTable).where(TagTable.tag == tag)
    result = session.exec(statement)
    tagT = result.one_or_none()

    if tagT: #found
       return tagT
    else: #not found
       return TagTable(tag=tag) # new instance



def create_record(post: Post) -> Post:
  # convert to PostTable
  postT = forward(post)

  # save to DB
  with Session(engine) as session:
    session.add(postT)
    # session.commit()
    session.refresh(postT)

  # convert back to Post
  updated_post = reverse(postT)

  return updated_post

def get_record(id: int) -> Post:
    pass

def update_record(post: Post) -> Post:
    pass

def delete_record(id: int) -> None:
    pass

