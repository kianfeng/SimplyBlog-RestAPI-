from sqlalchemy.orm import Session
from .. import schemas, models, hashing
from fastapi import HTTPException, status


def create(request: schemas.UserBase, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashing.get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get(user_id: int, db: Session):
    search_user = db.query(models.User).where(models.User.id == user_id).first()
    if not search_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user id {user_id} not found")
    return search_user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users
