from sqlmodel import SQLModel


class IUser(SQLModel):   # Schema not database
    nome: str
    email: str
