from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str]= None):
    # only get 10 published blogs
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unplished')
def unplished():
    return {'data':'all unplished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit: int = 10):
    return limit
    return {'data': {'1','2'}}


@app.post('/blog')
def create_blog():
    return {'data': "Blog is created"}