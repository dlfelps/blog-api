
from fastapi import FastAPI
from datetime import datetime

from models import Post

from pw_interface import create_record, delete_record, update_record, get_record

app = FastAPI()


@app.post("/posts/", status_code=201)
async def create_post(new_post: Post) -> Post:

  # add the created at time  
  new_post.createdAt = datetime.now()
  new_post.updatedAt = new_post.createdAt

  # save to db
  new_post = create_record(new_post)
  return new_post


@app.get("/posts/{id}", status_code=200)
async def get_post(id: int) -> Post:
  return get_record(id)

@app.put("/posts/{id}", status_code=200)
async def update_post(id: int, updated_post: Post) -> Post:
  updated_post = update_record(id, updated_post)
  return updated_post


@app.get("/posts/", status_code=200)
async def fetch_all_posts() -> list[Post]:
  pass

@app.delete("/posts/{id}", status_code=204)
async def delete_post_by(id: int) -> None:
  pass
