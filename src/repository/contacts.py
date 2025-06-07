from fastapi import HTTPException, status
from src.database.models import Contacts


async def get_contacts(db):
    return db.query(Contacts).all()


async def create_contact(body, db):
    contact = Contacts(**body.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_contact_by_id(id: int, db):
    contact = db.query(Contacts).filter_by(id=id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


async def update_contact(id: int, body, db):
    contact = db.query(Contacts).filter_by(id=id).first()

    for key, value in body.model_dump().items():
        setattr(contact, key, value)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(id: int, body, db):
    contact = db.query(Contacts).filter_by(id=id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )

    updated_data = body.model_dump()
    for key, value in updated_data.items():
        setattr(contact, key, value)

    db.commit()
    db.refresh(contact)
    return contact


async def delete_contact(id: int, db):
    contact = db.query(Contacts).filter_by(id=id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )

    db.delete(contact)
    db.commit()
    return contact
