from fastapi import Depends, FastAPI
from typing import Generator
from sqlalchemy.orm import Session
from User_Item_CRUD.Database.base import SessionLocal, engine
from User_Item_CRUD.Database import models, schemas
from User_Item_CRUD import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index() -> str:
    return "hello world"


@app.post("/users/", response_model=schemas.UserBase)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
