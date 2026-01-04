from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    public_key: str 
    plugs: List["InformationPlug"] = Relationship(back_populates="creator")

class InformationPlug(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    encryption_data: str 
    creator_id: int = Field(foreign_key="user.id")
    creator: User = Relationship(back_populates="plugs")
