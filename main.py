from typing import Union,Optional, List

from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI
from datetime import datetime

from post import Post

app = FastAPI()
# engine = create_engine("sqlite:///database.db")
# SQLModel.metadata.create_all(engine)

@app.post("/posts/", status_code=201)
async def create_post(post: Post) -> Post:
  # add the created at time
  post.createdAt = datetime.now()
  post.updatedAt = post.createdAt

  # with Session(engine) as session:
  #         session.add(post)
  #         session.commit()
  return post


@app.get("/posts/{id}", status_code=200)
async def fetch_post_by(id: int) -> Post:
  return Post(title=f"Post # {id}", content="default content", tags=["default"])

@app.get("/posts/", status_code=200)
async def fetch_all_posts() -> list[Post]:
  return [Post(title="Post #9", content="default content", tags=["default"]), Post(title="Post #10", content="default content", tags=["default"])]

@app.delete("/posts/{id}", status_code=204)
async def delete_post_by(id: int) -> None:
  pass
