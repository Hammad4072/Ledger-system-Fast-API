from sqlalchemy.orm import Session
from . import models, schemas

# Ledger Functions
def create_ledger(db: Session, ledger: schemas.LedgerCreate):
    db_ledger = models.Ledger(**ledger.dict())
    db.add(db_ledger)
    db.commit()
    db.refresh(db_ledger)
    return db_ledger

def get_ledgers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ledger).offset(skip).limit(limit).all()

# Stock Functions
def create_stock(db: Session, stock: schemas.StockCreate):
    db_stock = models.Stock(**stock.dict())
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def get_stocks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stock).offset(skip).limit(limit).all()