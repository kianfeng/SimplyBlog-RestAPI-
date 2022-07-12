from fastapi import Depends, APIRouter, status
from .. import schemas, database, oauth2
from ..repository import blogs
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

get_db = database.get_db


# current_user: schemas.UserBase = Depends(oauth2.get_current_user) use for add authentication/authorization for this endpoint
# if want to check access_token, in browser fn+f12 -> Network -> login in Authorize -> Name("login") -> preview
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.BlogBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blogs.create(request, db)


@router.put("/{blog_id}", status_code=status.HTTP_200_OK)
async def update(blog_id: int, request: schemas.BlogBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blogs.update(blog_id, request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
async def get_all_blogs(db: Session = Depends(get_db)):
    return blogs.get_all(db)


# already fixed validationError, use .all() with List, use .first with not list
@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return blogs.get(blog_id, db)


@router.delete("/{blog_id}", status_code=status.HTTP_200_OK)
async def delete(blog_id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return blogs.delete(blog_id, db)
