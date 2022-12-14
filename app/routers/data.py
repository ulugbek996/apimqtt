from datetime import date, timedelta

from fastapi import FastAPI , APIRouter ,Depends
from sqlalchemy import func
from sqlalchemy.orm import Session, lazyload
from ..database import get_db
from .. import models, schemas ,oauth2
from ..worker import change_str_tuple
from typing import List
from fastapi_pagination import Page, add_pagination, paginate
router = APIRouter(prefix="/data", tags=["Data"])


@router.get("/water/{id}")
def get_station_info(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    data_houre = db.query(models.WaterStationDataHour).filter(models.WaterStationDataHour.station_id == id).filter(func.date(models.WaterStationDataHour.time) == date.today()).all()
    return data_houre

@router.get("/well/{id}")
def get_station_info(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    data_houre = db.query(models.WellStationDataHour).filter(models.WellStationDataHour.station_id == id).filter(func.date(models.WellStationDataHour.time) == date.today()).all()
    return data_houre

@router.get("/water/between/{id}")
def get_station_data_between(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), date1:date = None, date2:date = None):
    data_houre = db.query(models.WaterStationDataHour).filter(models.WaterStationDataHour.station_id == id).filter(models.WaterStationDataHour.time.between(date1, date2)).all()
    return data_houre

@router.get("/well/between/{id}")
def get_station_data_between(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), date1:date = None, date2:date = None):
    data_houre = db.query(models.WellStationDataHour).filter(models.WellStationDataHour.station_id == id).filter(models.WellStationDataHour.time.between(date1, date2)).all()
    return data_houre

@router.get("/water/allday/{id}")
def get_station_data_day(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), day:int = None):
    data_houre = db.query(models.WaterStationDataHour).filter(models.WaterStationDataHour.station_id == id).filter(models.WaterStationDataHour.time > date.today() - timedelta(days=day)).all()
    return data_houre

@router.get("/well/allday/{id}")
def get_station_data_day(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), day:int = None):
    data_houre = db.query(models.WellStationDataHour).filter(models.WellStationDataHour.station_id == id).filter(models.WellStationDataHour.time > date.today() - timedelta(days=day)).all()
    return data_houre

@router.get("/water/day/{id}")
def get_station_data_day(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), date1:date = None):
    data_houre = db.query(models.WaterStationDataHour).filter(models.WaterStationDataHour.station_id == id).filter(func.date(models.WaterStationDataHour.time) == date1).all()
    return data_houre

@router.get("/well/day/{id}")
def get_station_data_day(id:int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user), date1:date = None):
    data_houre = db.query(models.WellStationDataHour).filter(models.WellStationDataHour.station_id == id).filter(func.date(models.WellStationDataHour.time) == date1).all()
    return data_houre