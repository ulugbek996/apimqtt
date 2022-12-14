from fastapi import FastAPI , APIRouter ,Depends
from fastapi_utils.tasks import repeat_every
from ..database import get_db , SessionLocal ,conn , engine , database
from .. import models, schemas
from .. worker import vaqt_uzgartirish , change_str_float
router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.on_event("startup")
@repeat_every(seconds=600, raise_exceptions=True)
async def task_water():
    data = conn.fastapi.data_water.find()
    for i in data:
        try:
            query = models.WaterStation1.select().where(models.WaterStation1.c.imei == i["imei"])
            my_station = await database.fetch_one(query=query)
            if my_station:
                data_shcemas = schemas.DataWaterWrite(**i)
                data_shcemas.station_id = my_station.id
                #data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
                #data_shcemas = schemas.DataWaterRead(**data_shcemas.dict())
                query = models.WaterStationDataHour1.insert().values(**data_shcemas.dict())
                last_record_id = await database.execute(query)
                query= models.WaterStationDataUpdate1.select().where(models.WaterStationDataUpdate1.c.station_id == my_station.id)
                my_station_data = await database.fetch_one(query=query)
                if my_station_data:
                    query = models.WaterStationDataUpdate1.update().where(models.WaterStationDataUpdate1.c.station_id == my_station.id).values(**data_shcemas.dict())
                    last_record_id = await database.execute(query)
                else:
                    query = models.WaterStationDataUpdate1.insert().values(**data_shcemas.dict())
                    last_record_id = await database.execute(query)
            conn.fastapi.data_water.delete_one({"_id": i["_id"]})
        except Exception as e:
            print(e)

@router.on_event("startup")
@repeat_every(seconds=3600, raise_exceptions=True)
async def task_info_water():
    info = conn.fastapi.water_info.find()
    for i in info:
        try:
            query = models.WaterStation1.select().where(models.WaterStation1.c.imei == i["imei"])
            my_station = await database.fetch_one(query=query)
            if my_station:
                i['signal'] = change_str_float(i['signal'])
                info_shcemas = schemas.AllStationInfo(**i)
                info_shcemas.station_id = my_station.id
                #info_shcemas.time = vaqt_uzgartirish(info_shcemas.time)
                query = models.WaterStationInfo1.insert().values(**info_shcemas.dict())
                last_record_id = await database.execute(query)
                query= models.WaterStationInfoUpdate1.select().where(models.WaterStationInfoUpdate1.c.station_id == my_station.id)
                my_station_data = await database.fetch_one(query=query)
                if my_station_data:
                    query = models.WaterStationInfoUpdate1.update().where(models.WaterStationInfoUpdate1.c.station_id == my_station.id).values(**info_shcemas.dict())
                    last_record_id = await database.execute(query)
                else:
                    query = models.WaterStationInfoUpdate1.insert().values(**info_shcemas.dict())
                    last_record_id = await database.execute(query)
            conn.fastapi.water_info.delete_one({"_id": i["_id"]})
        except Exception as e:
            print(e)

@router.on_event("startup")
@repeat_every(seconds=4600, raise_exceptions=True)
async def task_info_well():
    info = conn.fastapi.well_info.find()
    for i in info:
        try:
            query = models.WellStation1.select().where(models.WellStation1.c.imei == i["imei"])
            my_station = await database.fetch_one(query=query)
            if my_station:
                i['signal'] = change_str_float(i['signal'])
                info_shcemas = schemas.AllStationInfo(**i)
                info_shcemas.station_id = my_station.id
               # info_shcemas.time = vaqt_uzgartirish(info_shcemas.time)
                query = models.WellStationInfo1.insert().values(**info_shcemas.dict())
                last_record_id = await database.execute(query)
                query= models.WellStationInfoUpdate1.select().where(models.WellStationInfoUpdate1.c.station_id == my_station.id)
                my_station_data = await database.fetch_one(query=query)
                if my_station_data:
                    query = models.WellStationInfoUpdate1.update().where(models.WellStationInfoUpdate1.c.station_id == my_station.id).values(**info_shcemas.dict())
                    last_record_id = await database.execute(query)
                else:
                    query = models.WellStationInfoUpdate1.insert().values(**info_shcemas.dict())
                    last_record_id = await database.execute(query)
            conn.fastapi.well_info.delete_one({"_id": i["_id"]})
        except Exception as e:
            print(e)

@router.on_event("startup")
@repeat_every(seconds=5600, raise_exceptions=True)
async def task_well():
    data = conn.fastapi.data_well.find()
    for i in data:
        try:
            query = models.WellStation1.select().where(models.WellStation1.c.imei == i["imei"])
            my_station = await database.fetch_one(query=query)
            if my_station:
                data_shcemas = schemas.DataWellWrite(**i)
                data_shcemas.station_id = my_station.id
                #data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
                query = models.WellStationDataHour1.insert().values(**data_shcemas.dict())
                last_record_id = await database.execute(query)
                query= models.WellStationDataUpdate1.select().where(models.WellStationDataUpdate1.c.station_id == my_station.id)
                my_station_data = await database.fetch_one(query=query)
                if my_station_data:
                    query = models.WellStationDataUpdate1.update().where(models.WellStationDataUpdate1.c.station_id == my_station.id).values(**data_shcemas.dict())
                    last_record_id = await database.execute(query)
                else:
                    query = models.WellStationDataUpdate1.insert().values(**data_shcemas.dict())
                    last_record_id = await database.execute(query)
            conn.fastapi.data_well.delete_one({"_id": i["_id"]})
        except Exception as e:
            print(e)
