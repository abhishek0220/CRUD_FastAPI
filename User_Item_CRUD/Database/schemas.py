from datetime import datetime
from typing import List

from pydantic import BaseModel, validator
from hashlib import md5


class UserBase(BaseModel):
    email: str
    name: str
    dob: datetime

    @validator('dob', pre=True)
    def dob_check(cls, v: List[int]):
        try:
            _dob = datetime(day=v[0], month=v[1], year=v[2])
        except ValueError as e:
            raise e
        if _dob >= datetime.now():
            raise ValueError("Future Date")
        return _dob


class UserCreate(UserBase):
    password: str

    @validator('password', pre=True)
    def pw_creation(cls, v: str):
        if len(v) < 5:
            raise ValueError("Password too short")
        hashed_pw = md5(v.encode()).hexdigest()
        return hashed_pw


sample_user = {
    "name": "Abhishek",
    "email": "2018ucs0087@iitjammu.ac.in",
    "password": "123456",
    "dob": (20, 2, 2000)
}
