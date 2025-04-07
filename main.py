from fastapi import FastAPI, Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

# creating a model by pydantic
# pydantic is a data validation 
class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating : Optional[int] = None

@app.get("/")
async def root():
    return {"message":"hello world from fastapi app"}


@app.post("/createposts",status_code=status.HTTP_201_CREATED)
async def create_posts(new_post:Post):
    print(new_post)
    print(new_post.model_dump())
    print(new_post.dict(),"dictionary method")
    return {"message":f" name is {new_post.title} created"}

@app.get("/posts/latest")
async def get_latest_post():
    return {"post_id":1,"title":"latest post"}

@app.get("/posts/{id}")
async def get_post(id:int,response:Response):

    if id > 5:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":"post not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found {id}")
    return {"post_id":id}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    # delete post logic
    return Response(status_code=status.HTTP_204_NO_CONTENT)
