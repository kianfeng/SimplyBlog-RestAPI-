from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, models, hashing, database, token

router = APIRouter(
    tags=["Authentication"]
)

get_db = database.get_db


# copy from official doc OAuth2 @app.post("/token")
@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(request.username == models.User.email).first()
    # verify username(email) by verifying object user exist
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"username {request.username} not found")
    # verify user password by verifying object user's password
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"password {request.password} is incorrect")

    # create JWT access token, [copy from office docs @app.post("/token")]
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
