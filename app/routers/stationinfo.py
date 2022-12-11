from fastapi import FastAPI , APIRouter ,Depends
from sqlalchemy.orm import Session, lazyload
from ..database import get_db
from .. import models, schemas ,oauth2
from ..worker import change_str_tuple
from typing import List
from fastapi_pagination import Page, add_pagination, paginate
router = APIRouter(prefix="/stationinfo", tags=["stationinfo"])


@router.get("/get" , response_model=Page[schemas.WaterStationOut])
#@router.get("/get" )
def get_station_info(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    tuple = change_str_tuple(station_list.station_list)
    station = db.query(models.WaterStation).filter(models.WaterStation.id.in_((tuple))).all()
    return paginate(station)


add_pagination(router)

