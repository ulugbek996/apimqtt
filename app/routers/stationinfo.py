from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas ,oauth2
from ..worker import change_str_tuple
from typing import Union
from fastapi_pagination import Page, add_pagination, paginate
router = APIRouter(prefix="/stationinfo", tags=["stationinfo"])


@router.get("/water" , response_model=Page[schemas.WaterStationOut] )
def get_station_info(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user) ,info_time:str = None ):
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    tuple = change_str_tuple(station_list.water_station_list)
    station = db.query(models.WaterStation).filter(models.WaterStation.id.in_(tuple)).all()

    return paginate(station)

@router.get("/well" , response_model=Page[schemas.WellStationOut])
def get_station_info(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    tuple = change_str_tuple(station_list.well_station_list)
    station = db.query(models.WellStation).filter(models.WellStation.id.in_((tuple))).all()
    return paginate(station)


add_pagination(router)

