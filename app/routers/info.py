from datetime import date
from fastapi import FastAPI , APIRouter ,Depends
from sqlalchemy import func
from sqlalchemy.orm import Session, lazyload
from ..database import get_db
from .. import models, schemas ,oauth2
from ..worker import change_str_tuple
from typing import List
from fastapi_pagination import Page, add_pagination, paginate
router = APIRouter(prefix="/info", tags=["Info"])


@router.get("/water/{id}")
def get_station_info(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    station = db.query(models.WaterStationInfo).filter(models.WaterStationInfo.station_id == id).filter(func.date(models.WaterStationInfo.time) == date.today()).all()
    return station

@router.get("/well/{id}")
def get_station_info(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    station = db.query(models.WellStationInfo).filter(models.WellStationInfo.station_id == id).filter(func.date(models.WellStationInfo.time) == date.today()).all()
    return station


