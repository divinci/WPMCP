from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from . import wordpress

app = FastAPI(title="WPMCP")


class PostCreate(BaseModel):
    title: str
    content: str
    status: str = "draft"


@app.get("/posts")
def get_posts():
    try:
        return wordpress.list_posts()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/posts")
def create_post(post: PostCreate):
    try:
        return wordpress.create_post(post.title, post.content, post.status)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
