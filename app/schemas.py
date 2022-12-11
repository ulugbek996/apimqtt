from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional, List


class DataWaterInput(BaseModel):
    imei: int = Field(alias="i")
    time: str = Field(alias="t")
    level: float = Field(alias="d")
    flow: float = Field(alias="v")
    correction: int = Field(alias="c")


class DataWellInput(BaseModel):
    imei: int = Field(alias="i")
    time: str = Field(alias="t")
    level: float = Field(alias="d")
    meloration: float = Field(alias="r")
    tempratura: int = Field(alias="q")

class DataWrite(BaseModel):
    station_id: Optional[int]
    time: str
    level: float
    flow: float
    correction: int

class StationInfoInput(BaseModel):
    imei: int = Field(alias="i")
    time: str = Field(alias="t")
    region_id: str = Field(alias="p1")
    balans_id: str = Field(alias="p2")
    name: str = Field(alias="p3")
    tel_seria: str = Field(alias="p4")
    tel_number: str = Field(alias="p5")
    locatsiya: str = Field(alias="p6")
    tempratura: float = Field(alias="p7")
    bateriya: float = Field(alias="p8")
    signal: str = Field(alias="p9")
    proshivka: str = Field(alias="p10")
    frivers: str = Field(alias="p11")
    time1: int = Field(alias="p12")
    time2: int = Field(alias="p13")
    time3: int = Field(alias="p14")
    time4: int = Field(alias="p15")
    sensor_id: str = Field(alias="p16")
    sensor_name: Optional[str] = Field(alias="p17")

class WaterStationInfo(BaseModel):
    station_id : Optional[int]
    time: str
    bateriya: float
    signal: float
    tempratura: float
    proshivka: str
    frivers: str
    locatsiya: str
    time1: int
    time2: int
    time3: int
    time4: int

class WaterStationInfoUpdate(BaseModel):
    time: str
    bateriya: int
    signal: float
    tempratura: int
    proshivka: str
    frivers: str
    locatsiya: str
    time1: str
    time2: str
    time3: str
    time4: str

class WaterStationDataUpdateOut(BaseModel):
    time: str
    level: float
    flow: float
    correction: int

    class Config:
        orm_mode = True

class WaterStationInfoOut(BaseModel):
    time: str
    bateriya: float
    signal: float
    tempratura: float
    proshivka: str
    frivers: str
    locatsiya: str
    time1: int
    time2: int
    time3: int
    time4: int

    class Config:
        orm_mode = True



class Balans(BaseModel):
    id: int
    name: str
    region_id: int

    class Config:
        orm_mode = True

class Region(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Sensor(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class District(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class WaterStationOut(BaseModel):
    id: int
    imei: int
    name: str
    balans: Balans
    region: Region
    sensor: Sensor
    district: District
    water_station_info_update: List[WaterStationInfoOut]
    water_station_data_update: List[WaterStationDataUpdateOut]
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    id: Optional[str] = None


class Alert2(BaseModel):
    imei: int = Field(alias="i")
    time: str = Field(alias="t")
    region_id: str = Field(alias="p1")
    balans_id: str = Field(alias="p2")
    name: str = Field(alias="p3")
    tel_seria: str = Field(alias="p4")
    tel_number: str = Field(alias="p5")
    locatsiya: str = Field(alias="p6")
    status: str = Field(alias="p7")

class WaterStationCreate(BaseModel):
    imei: int
    name: str
    balans_id: int
    region_id: int
    sensor_id: int
    district_id: int
    lat: float
    lon: float
    telphone_sensor: str
    telphone_balans: str
