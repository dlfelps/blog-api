# Blogging Platform API

![Blogging Platform API](https://assets.roadmap.sh/guest/blogging-platform-api.png)

This project implements a RESTful API with basic CRUD operations for a personal blogging platform. It is written in Python using [FastAPI](https://fastapi.tiangolo.com/) to provide the REST interface and [peewee](https://docs.peewee-orm.com/en/latest/) to interface with SQLite.

NOTE: This project does not implement a frontend client. The backend web service sends/recieves posts in JSON form. 

## Goals
The goals of this project are to:
- Demonstrate RESTful APIs and their best practices and conventions
- Demonstrate CRUD operations using an Object Relational Model (ORM)



## Blog capabilities
The RESTful API allows users to perform the following operations:
- Create a new blog post
- Get a single blog post
- Get all blog posts
- Filter blog posts by tag
- Update an existing blog post
- Delete an existing blog post

## Installation
1. Clone the repo (git clone https://github.com/dlfelps/blog-api.git)
2. Install dependencies (pip install -r requirements.txt)
3. Initialize the ASGI web server (fastapi dev ./main.py)

## Organization of code
The code is divided between two files:
- main.py contains all of the [FastAPI](https://fastapi.tiangolo.com/) code to create the REST interface
- db_interface.py contains all of the [peewee](https://docs.peewee-orm.com/en/latest/) code to interface with the database

If you would like to modify this code to use a different database, peewee currently supports:
- Postgres
- MySQL
- MariaDB
- SQLite
- CockroachDB

If you would like to use a different ORM (e.g. [SQLAlchemy](https://www.sqlalchemy.org/) or [SQLModel](https://sqlmodel.tiangolo.com/)), you can replace db_interface.py with your own (e.g. db2_interface.py) following the function interfaces as designed.

## Examples

### Create Blog Post
Create a new blog post using the POST method

```json
POST /posts
{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}
```

The endpoint should validate the request body and return a `201 Created` status code with the newly created blog post :

```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```
or a `400 Bad Request` status code with error messages in case of validation errors.

### Get Blog Post
Get a single blog post using the GET method

```
GET /posts/1
```
The endpoint should return a `200 OK` status code with the blog post:
```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```
or a `404 Not Found` status code if the blog post was not found.

### Get All Blog Posts
Get all blog posts using the GET method
```
GET /posts
```
The endpoint should return a `200 OK` status code with an array of blog posts i.e.
```json
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:00:00Z"
  },
  {
    "id": 2,
    "title": "My Second Blog Post",
    "content": "This is the content of my second blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "createdAt": "2021-09-01T12:30:00Z",
    "updatedAt": "2021-09-01T12:30:00Z"
  }
]
```

### Filter blog posts by tag
While retrieving posts, user can also filter posts by their associated tags. You can retrieve posts that only have the specified tag:

```
GET /posts?tag=tech
```

This should return all blog posts that are tagged with “tech”.

### Update Blog Post
Update an existing blog post using the PUT method

```json
PUT /posts/1
{
  "title": "My Updated Blog Post",
  "content": "This is the updated content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}
```

The endpoint should validate the request body and return a `200 OK` status code with the updated blog post

```json
{
  "id": 1,
  "title": "My Updated Blog Post",
  "content": "This is the updated content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:30:00Z"
}
```

or a `400 Bad Request` status code with error messages in case of validation errors. It should return a `404 Not Found` status code if the blog post was not found.

### Delete Blog Post
Delete an existing blog post using the DELETE method
```
DELETE /posts/1
```
The endpoint should return a `204 No Content` status code if the blog post was successfully deleted or a `404 Not Found` status code if the blog post was not found.
