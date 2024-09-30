
from fastapi import FastAPI
from datetime import datetime

from models import Post

from pw_interface import create_record, delete_record, update_record, get_record

app = FastAPI()


@app.post("/posts/", status_code=201)
async def create_post(post: Post) -> Post:

  # add the created at time  
  post.createdAt = datetime.now()
  post.updatedAt = post.createdAt

  # save to db
  post = create_record(post)
  return post


@app.get("/posts/{id}", status_code=200)
async def fetch_post_by(id: int) -> Post:
  return get_record(id)

@app.get("/posts/", status_code=200)
async def fetch_all_posts() -> list[Post]:
  return [Post(title="Post #9", content="default content", tags=["default"]), Post(title="Post #10", content="default content", tags=["default"])]

@app.delete("/posts/{id}", status_code=204)
async def delete_post_by(id: int) -> None:
  pass
