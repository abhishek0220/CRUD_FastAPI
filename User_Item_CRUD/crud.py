from sqlalchemy.orm import Session
from User_Item_CRUD.Database import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> None:
    db_user = models.User(**user.dict())
    db_user.save_to_db(db)
