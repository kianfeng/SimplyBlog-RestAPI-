from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import HTTPException, status


def create(request: schemas.BlogBase, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    # add that instance object to your database session.
    db.add(new_blog)
    # commit the changes to the database (so that they are saved).
    db.commit()
    # refresh your instance (so that it contains any new data from the database, like the generated ID).
    db.refresh(new_blog)
    return new_blog


def update(blog_id: int, request: schemas.BlogBase, db: Session):
    current_blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not current_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"id {blog_id} not exists")

        # update method 1: convert model to a dictionary
        # current_blog.update(request.dict())

        # update method 2: declare each attribute in object
    current_blog.update({'title': request.title, 'body': request.body})

    db.commit()
    return request


def get_all(db: Session):
    all_blogs = db.query(models.Blog).all()
    return all_blogs


def get(blog_id: int, db: Session):
    search_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not search_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog id {blog_id} not found")
    return search_blog


def delete(blog_id: int, db: Session):
    db.query(models.Blog).filter(models.Blog.id == blog_id). \
        delete(synchronize_session=False)
    db.commit()
    return "delete success"
