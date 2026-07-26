from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
def index(limit):
    # only get 10 published blogs
    return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unplished')
def unplished():
    return {'data':'all unplished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}