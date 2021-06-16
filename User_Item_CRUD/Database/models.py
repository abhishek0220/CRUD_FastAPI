from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime
from sqlalchemy.orm import relationship, Session, RelationshipProperty
from User_Item_CRUD.Database.base import Base

user_item_table = Table(
    'user_item_table', Base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('items_id', Integer, ForeignKey('items.id'))
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    dob = Column(DateTime)
    password = Column(String)
    items: RelationshipProperty = relationship(
        "Item",
        secondary=user_item_table,
        back_populates="users"
    )

    def save_to_db(self, db: Session) -> None:
        db.add(self)
        db.commit()
        db.refresh(self)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users: RelationshipProperty = relationship(
        "User",
        secondary=user_item_table,
        back_populates="items"
    )
