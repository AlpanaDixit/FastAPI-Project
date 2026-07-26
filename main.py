from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}

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