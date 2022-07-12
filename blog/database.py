from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# todo: use mysql later
# SQLALCHEMY_DATABASE_URL = "mysql://user:password@postgresserver/db"

# create a SQLAlchemy "engine".
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

# instance of actual database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base used to create the SQLAlchemy models.
Base = declarative_base()


# helper function to create dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()