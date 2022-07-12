from fastapi import Depends, APIRouter, status
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from ..repository import users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

get_db = database.get_db


# todo: difference between post and put
@router.post("/", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
async def create_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    return users.create(request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
async def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return users.get(user_id, db)
