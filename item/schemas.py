from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    price: int
    amount: int

    class Config:
        orm_mode = True


class ItemList(ItemBase):
    id: int


class ItemCreate(ItemBase):
    pass
