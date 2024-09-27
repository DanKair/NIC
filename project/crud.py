from sqlalchemy.orm import Session
from project import models, schemas

# Create an item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Get all items
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()


# Get an item by ID
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


# Update an item
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item


# Delete an item
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
