from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas

app = FastAPI()



@app.post('/blog')
def create(request: schemas.Blog):
    # return 'creating'
    # return {'title': title, 'body': body}
    return request