
from fastapi import FastAPI, HTTPException
from datetime import datetime
from models import Post

from db_interface import create_record, delete_record, update_record, get_record_by_tag, get_record_by_id, get_all_records

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
  post = get_record_by_id(id)
  if post:
    return post
  else:
    raise HTTPException(status_code=404, detail="Post not found")


@app.get("/posts/", status_code=200)
async def get_post(tag: str | None = None) -> list[Post]:
  if tag:
    return get_record_by_tag(tag)
  else:
    return get_all_records()

@app.put("/posts/{id}", status_code=200)
async def update_post(id: int, updated_post: Post) -> Post:
  updated_post = update_record(id, updated_post)
  return updated_post


@app.delete("/posts/{id}", status_code=204)
async def delete_post_by(id: int) -> None:
  if delete_record(id): 
    return None
  else:
    raise HTTPException(status_code=404, detail="Post not found")
