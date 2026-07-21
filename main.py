from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name': 'Alpana', 'age': '29'}}

@app.get('/about')
def about():
    return {'data': 'about page'}

