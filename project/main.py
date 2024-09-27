from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from project import models, schemas, crud, database
from .database import engine, get_db

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="REST API with CRUD", description="Made by Kair", debug=True
)

# Create an item
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: Annotated[schemas.ItemCreate, Depends()], db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


# Read all items
@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)


# Read a single item
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item_id(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Update an item
@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: Annotated[schemas.ItemCreate, Depends()], db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Delete an item
@app.delete("/items/{item_id}", response_model=schemas.ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
