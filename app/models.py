from  sqlalchemy import Column,Table, Integer, String, Float, Boolean, BigInteger, ForeignKey, MetaData, TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
metadata = MetaData()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))




class WaterStation(Base):
    __tablename__ = "water_stations"
    id = Column(Integer, primary_key=True, index=True)
    region_id =Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"), nullable=False)
    balans_id =Column(Integer, ForeignKey(
        "tashkilot.id", ondelete="CASCADE"), nullable=False)
    district_id = Column(Integer, ForeignKey(
        "districts.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, index=True)
    imei = Column(BigInteger, unique=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    sensor_id = Column(Integer, ForeignKey(
        "sensors.id", ondelete="CASCADE"), nullable=False)
    telphone_sensor = Column(String)
    telphone_balans = Column(String)
    status = Column(Boolean, server_default=text('true'))
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))
    district = relationship("District")
    balans = relationship("Balans")
    region = relationship("Region")
    sensor = relationship("Sensor")
    water_station_info_update = relationship("WaterStationInfoUpdate")
    water_station_data_update = relationship("WaterStationDataUpdate")



class WellStation(Base):
    __tablename__ = "well_stations"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    balans_id = Column(Integer, ForeignKey("tashkilot.id"))
    district_id = Column(Integer, ForeignKey("districts.id"))
    name = Column(String, index=True)
    imei = Column(BigInteger, unique=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    telphone_sensor = Column(String)
    telphone_balans = Column(String)
    status = Column(Boolean, server_default=text('true'))
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))



class WaterStationInfo(Base):
    __tablename__ = "water_station_info"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("water_stations.id"))
    time = Column(String)
    bateriya = Column(Float)
    signal = Column(Float)
    locatsiya = Column(String)
    tempratura = Column(Float)
    proshivka = Column(String)
    frivers = Column(String)
    time1 = Column(Integer)
    time2 = Column(Integer)
    time3 = Column(Integer)
    time4 = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=text('now()'))

class WellStationInfo(Base):
    __tablename__ = "well_station_info"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("well_stations.id"))
    time = Column(String)
    bateriya = Column(Float)
    signal = Column(Float)
    locatsiya = Column(String)
    tempratura = Column(Float)
    proshivka = Column(String)
    frivers = Column(String)
    time1 = Column(Integer)
    time2 = Column(Integer)
    time3 = Column(Integer)
    time4 = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=text('now()'))

class WaterStationInfoUpdate(Base):
    __tablename__ = "water_station_info_update"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("water_stations.id"))
    time = Column(String)
    bateriya = Column(Float)
    signal = Column(Float)
    locatsiya = Column(String)
    tempratura = Column(Float)
    proshivka = Column(String)
    frivers = Column(String)
    time1 = Column(Integer)
    time2 = Column(Integer)
    time3 = Column(Integer)
    time4 = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))

class WellStationInfoUpdate(Base):
    __tablename__ = "well_station_info_update"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("well_stations.id"))
    time = Column(String)
    bateriya = Column(Float)
    signal = Column(Float)
    locatsiya = Column(String)
    tempratura = Column(Float)
    proshivka = Column(String)
    frivers = Column(String)
    time1 = Column(Integer)
    time2 = Column(Integer)
    time3 = Column(Integer)
    time4 = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))

class WaterStationDataHour(Base):
    __tablename__ = "water_station_data_hour"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("water_stations.id"))
    time = Column(String)
    level = Column(Float)
    flow = Column(Float)
    correction = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('now()'))

class WellStationDataHour(Base):
    __tablename__ = "well_station_data_hour"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("well_stations.id"))
    time = Column(String)
    level = Column(Float)
    meloration = Column(Float)
    tempratura = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('now()'))

class WaterStationDataDay(Base):
    __tablename__ = "water_station_data_day"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("water_stations.id"))
    time = Column(String)
    level = Column(Float)
    flow = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('now()'))

class WellStationDataDay(Base):
    __tablename__ = "well_station_data_day"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("well_stations.id"))
    time = Column(String)
    level = Column(Float)
    meloration = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('now()'))

class WaterStationDataUpdate(Base):
    __tablename__ = "water_station_data_update"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("water_stations.id"))
    time = Column(String)
    level = Column(Float)
    flow = Column(Float)
    correction = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))

class WellStationDataUpdate(Base):
    __tablename__ = "well_station_data_update"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("well_stations.id"))
    time = Column(String)
    level = Column(Float)
    meloration = Column(Float)
    tempratura = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))


class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Balans(Base):
    __tablename__ = "tashkilot"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    name = Column(String, unique=True, index=True)

class District(Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    name = Column(String, unique=True, index=True)

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class UserStation(Base):
    __tablename__ = "user_stations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    station_list = Column(String)
    created_at = Column(TIMESTAMP, server_default=text('now()'))


WaterStation1 = Table(
    "water_stations",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("region_id", Integer, ForeignKey("regions.id")),
    Column("balans_id", Integer, ForeignKey("tashkilot.id")),
    Column("district_id", Integer, ForeignKey("districts.id")),
    Column("name", String),
    Column("imei", BigInteger, unique=True, index=True),
    Column("lat", Float),
    Column("lon", Float),
    Column("sensor_id", Integer, ForeignKey("sensors.id")),
    Column("telphone_sensor", String),
    Column("telphone_balans", String),
    Column("status", Boolean, server_default=text('true')),
    Column("created_at", TIMESTAMP, server_default=text('now()')),
    Column("updated_at", TIMESTAMP, server_default=text('now()')),

)
WaterStationDataHour1 = Table(
    "water_station_data_hour",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("station_id", Integer, ForeignKey("water_stations.id")),
    Column("time", String),
    Column("level", Float),
    Column("flow", Float),
    Column("correction", Float),
    Column("created_at", TIMESTAMP, server_default=text('now()')),
)
WaterStationDataUpdate1 = Table(
    "water_station_data_update",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("station_id", Integer, ForeignKey("water_stations.id")),
    Column("time", String),
    Column("level", Float),
    Column("flow", Float),
    Column("correction", Float),
    Column("created_at", TIMESTAMP, server_default=text('now()')),
    Column("updated_at", TIMESTAMP, server_default=text('now()')),
)

WaterStationInfo1 = Table(
    "water_station_info",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("station_id", Integer, ForeignKey("water_stations.id")),
    Column("time", String),
    Column("bateriya", Float),
    Column("signal", Float),
    Column("locatsiya", String),
    Column("tempratura", Float),
    Column("proshivka", String),
    Column("frivers", String),
    Column("time1", Integer),
    Column("time2", Integer),
    Column("time3", Integer),
    Column("time4", Integer),
    Column("created_at", TIMESTAMP, server_default=text('now()'))
)

WaterStationInfoUpdate1 = Table(
    "water_station_info_update",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("station_id", Integer, ForeignKey("water_stations.id")),
    Column("time", String),
    Column("bateriya", Float),
    Column("signal", Float),
    Column("locatsiya", String),
    Column("tempratura", Float),
    Column("proshivka", String),
    Column("frivers", String),
    Column("time1", Integer),
    Column("time2", Integer),
    Column("time3", Integer),
    Column("time4", Integer),
    Column("created_at", TIMESTAMP, server_default=text('now()')),
    Column("updated_at", TIMESTAMP, server_default=text('now()'))
)