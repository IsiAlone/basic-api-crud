from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI(    
    title = 'DEPLOY BASIC API CRUD',
    version = '0.1',
    openapi_tags = [{
        'name': 'BASIC POST API',
        'description': 'Esta API utiliza las peticiones basicas HTTP y se encuentra desplegada en Heroku'
    }]
)

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: bool=False

posts=[]

@app.get('/')
def read_root():
    return {'welcome': 'welcome 2'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post:Post):
    post.id=str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post

    raise HTTPException(status_code=404, detail='Post not found')

@app.delete('/posts/{posts_id}')
def delete_post(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
        return 'post eliminado'

    raise HTTPException(status_code=404, detail='Post not found')

@app.get('/post/{post_id}')
def get_post_id_2(post_id: str):
    for index,post in enumerate(posts):
        if post['id'] == post_id:
            ind=index
        return f'{ind}'

@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]['title'] == updatedPost.title
            print(index)
            print(updatedPost.title)
            posts[index]['author'] == updatedPost.author
            print(updatedPost.author)
            posts[index]['content'] == updatedPost.content
            return {'mensaje':'El post ha sido actualizado'}

    raise HTTPException(status_code=404, detail='Post not found')