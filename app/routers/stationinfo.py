from fastapi import APIRouter ,Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas ,oauth2
from ..worker import change_str_tuple
from typing import Union
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.sql import text
router = APIRouter(prefix="/stationinfo", tags=["stationinfo"])
from datetime import datetime , timedelta , date
from sqlalchemy import func
import json
@router.get("/water" , response_model=Page[schemas.WaterStationOut] )
def get_station_info(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user) ,sorting:str = None ):
    sort = schemas.WaterSorting.get(1)
    sort_json = json.dumps(sort.__dict__)
    try:
        sort_json = json.loads(sort_json)
        b = sort_json[sorting]
    except:
        b = "water_stations.id ASC"
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    if not station_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga qurilma qo'shilmagan")
    tuple = change_str_tuple(station_list.water_station_list)
    if not tuple:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga water qurilma qo'shilmagan")
    station = db.query(models.WaterStation).join(models.WaterStationDataUpdate ,isouter=True ).join(models.WaterStationInfoUpdate , isouter=True).filter(models.WaterStation.id.in_(tuple)).order_by(text(b)).all()
    return paginate(station)

@router.get("/well" , response_model=Page[schemas.WellStationOut])
def get_station_info(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user) ,sorting:str = None ):
    sort = schemas.WellSorting.get(1)
    sort_json = json.dumps(sort.__dict__)
    try:
        sort_json = json.loads(sort_json)
        b = sort_json[sorting]
    except Exception as e:
        b = "well_stations.id ASC"
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    if not station_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga qurilma qo'shilmagan")
    tuple = change_str_tuple(station_list.well_station_list)
    if not tuple:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga well qurilma qo'shilmagan")
    station = db.query(models.WellStation).join(models.WellStationInfoUpdate, isouter=True).join(models.WellStationDataUpdate , isouter=True).filter(models.WellStation.id.in_(tuple)).order_by(text(b)).all()
    return paginate(station)

@router.get("/water/status" , response_model= schemas.StationStatus)
def get_station_info_status(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    if not station_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga qurilma qo'shilmagan")
    tuple = change_str_tuple(station_list.water_station_list)
    if not tuple:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga water qurilma qo'shilmagan")
    info_day = db.query(func.count(models.WaterStationInfoUpdate.id)).filter(models.WaterStationInfoUpdate.station_id.in_(tuple)).filter(models.WaterStationInfoUpdate.time > date.today() - timedelta(days=1)).scalar()
    info_three_day = db.query(func.count(models.WaterStationInfoUpdate.id)).filter(models.WaterStationInfoUpdate.station_id.in_(tuple)).filter(models.WaterStationInfoUpdate.time > date.today() - timedelta(days=3)).scalar()
    info_week = db.query(func.count(models.WaterStationInfoUpdate.id)).filter(models.WaterStationInfoUpdate.station_id.in_(tuple)).filter(models.WaterStationInfoUpdate.time > date.today() - timedelta(days=7)).scalar()
    info_month = db.query(func.count(models.WaterStationInfoUpdate.id)).filter(models.WaterStationInfoUpdate.station_id.in_(tuple)).filter(models.WaterStationInfoUpdate.time > date.today() - timedelta(days=30)).scalar()
    info_year = db.query(func.count(models.WaterStationInfoUpdate.id)).filter(models.WaterStationInfoUpdate.station_id.in_(tuple)).filter(models.WaterStationInfoUpdate.time > date.today() - timedelta(days=365)).scalar()
    data_day = db.query(func.count(models.WaterStationDataUpdate.id)).filter(models.WaterStationDataUpdate.station_id.in_(tuple)).filter(models.WaterStationDataUpdate.time > date.today() - timedelta(days=1)).scalar()
    data_three_day = db.query(func.count(models.WaterStationDataUpdate.id)).filter(models.WaterStationDataUpdate.station_id.in_(tuple)).filter(models.WaterStationDataUpdate.time > date.today() - timedelta(days=3)).scalar()
    data_week = db.query(func.count(models.WaterStationDataUpdate.id)).filter(models.WaterStationDataUpdate.station_id.in_(tuple)).filter(models.WaterStationDataUpdate.time > date.today() - timedelta(days=7)).scalar()
    data_month = db.query(func.count(models.WaterStationDataUpdate.id)).filter(models.WaterStationDataUpdate.station_id.in_(tuple)).filter(models.WaterStationDataUpdate.time > date.today() - timedelta(days=30)).scalar()
    data_year = db.query(func.count(models.WaterStationDataUpdate.id)).filter(models.WaterStationDataUpdate.station_id.in_(tuple)).filter(models.WaterStationDataUpdate.time > date.today() - timedelta(days=365)).scalar()
    station = db.query(func.count(models.WaterStation.id)).filter(models.WaterStation.id.in_(tuple)).scalar()
    data = schemas.StationStatus(info_day=info_day,info_three_day=info_three_day,info_week=info_week,info_month=info_month,info_year=info_year,data_day=data_day,data_three_day=data_three_day,data_week=data_week,data_month=data_month,data_year=data_year,station=station)
    return data

@router.get("/well/status" , response_model= schemas.StationStatus)
def get_station_info_status(db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    station_list = db.query(models.UserStation).filter(models.UserStation.user_id == current_user.id).first()
    if not station_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga qurilma qo'shilmagan")
    try:
        tuple = change_str_tuple(station_list.well_station_list)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga well qurilma qo'shilmagan")
    if not tuple:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userga well qurilma qo'shilmagan")
    info_day = db.query(func.count(models.WellStationInfoUpdate.id)).filter(models.WellStationInfoUpdate.station_id.in_(tuple)).filter(models.WellStationInfoUpdate.time > date.today() - timedelta(days=1)).scalar()
    info_three_day = db.query(func.count(models.WellStationInfoUpdate.id)).filter(models.WellStationInfoUpdate.station_id.in_(tuple)).filter(models.WellStationInfoUpdate.time > date.today() - timedelta(days=3)).scalar()
    info_week = db.query(func.count(models.WellStationInfoUpdate.id)).filter(models.WellStationInfoUpdate.station_id.in_(tuple)).filter(models.WellStationInfoUpdate.time > date.today() - timedelta(days=7)).scalar()
    info_month = db.query(func.count(models.WellStationInfoUpdate.id)).filter(models.WellStationInfoUpdate.station_id.in_(tuple)).filter(models.WellStationInfoUpdate.time > date.today() - timedelta(days=30)).scalar()
    info_year = db.query(func.count(models.WellStationInfoUpdate.id)).filter(models.WellStationInfoUpdate.station_id.in_(tuple)).filter(models.WellStationInfoUpdate.time > date.today() - timedelta(days=365)).scalar()
    data_day = db.query(func.count(models.WellStationDataUpdate.id)).filter(models.WellStationDataUpdate.station_id.in_(tuple)).filter(models.WellStationDataUpdate.time > date.today() - timedelta(days=1)).scalar()
    data_three_day = db.query(func.count(models.WellStationDataUpdate.id)).filter(models.WellStationDataUpdate.station_id.in_(tuple)).filter(models.WellStationDataUpdate.time > date.today() - timedelta(days=3)).scalar()
    data_week = db.query(func.count(models.WellStationDataUpdate.id)).filter(models.WellStationDataUpdate.station_id.in_(tuple)).filter(models.WellStationDataUpdate.time > date.today() - timedelta(days=7)).scalar()
    data_month = db.query(func.count(models.WellStationDataUpdate.id)).filter(models.WellStationDataUpdate.station_id.in_(tuple)).filter(models.WellStationDataUpdate.time > date.today() - timedelta(days=30)).scalar()
    data_year = db.query(func.count(models.WellStationDataUpdate.id)).filter(models.WellStationDataUpdate.station_id.in_(tuple)).filter(models.WellStationDataUpdate.time > date.today() - timedelta(days=365)).scalar()
    station = db.query(func.count(models.WellStation.id)).filter(models.WellStation.id.in_(tuple)).scalar()
    data = schemas.StationStatus(info_day=info_day,info_three_day=info_three_day,info_week=info_week,info_month=info_month,info_year=info_year,data_day=data_day,data_three_day=data_three_day,data_week=data_week,data_month=data_month,data_year=data_year,station=station)
    return data
add_pagination(router)

