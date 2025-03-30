from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

# creating a model by pydantic
# pydantic is a data validation 
class Post(BaseModel):
    title:str
    content:str
    published:bool = True

@app.get("/")
async def root():
    return {"message":"hello world from fastapi app"}


@app.post("/createposts")
async def create_posts(new_post:Post):
    print(new_post)
    return {"message":f" name is {new_post.title} created"}