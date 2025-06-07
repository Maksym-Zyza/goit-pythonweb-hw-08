
from fastapi import APIRouter, Depends
from src.database.db import get_db

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get("/")

async def get_contacts(db = Depends(get_db)):
  return {"message": "get contacts"}