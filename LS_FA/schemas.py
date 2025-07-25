from pydantic import BaseModel

class LedgerBase(BaseModel):
    description: str
    amount: float

class LedgerCreate(LedgerBase):
    pass

class LedgerOut(LedgerBase):
    id: int

    class Config:
        orm_mode = True

class StockBase(BaseModel):
    name: str
    quantity: int

class StockCreate(StockBase):
    pass

class StockOut(StockBase):
    id: int

    class Config:
        orm_mode = True
