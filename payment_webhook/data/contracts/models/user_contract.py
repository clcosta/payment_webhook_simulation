from sqlmodel import SQLModel

class IUser(SQLModel): # Schema not database
    email: str
    password: str
    access_aproved: bool = False

