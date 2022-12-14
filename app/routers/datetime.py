from fastapi import FastAPI , APIRouter ,Depends
from sqlalchemy.orm import Session, lazyload
from ..database import get_db
from .. import models, schemas ,oauth2
from ..worker import change_str_tuple
from typing import List
from fastapi_pagination import Page, add_pagination, paginate
router = APIRouter(prefix="/datetime", tags=["Datetime"])


@router.post('/create')
def create_time(date_time:schemas.VaqtTest, db: Session = Depends(get_db)):
    new_time = models.VaqtTest(**date_time.dict())
    db.add(new_time)
    db.commit()
    db.refresh(new_time)
    return new_time

