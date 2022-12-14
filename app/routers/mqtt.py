from fastapi import FastAPI , APIRouter
from fastapi_mqtt import FastMQTT, MQTTConfig
from .. import models,schemas
import json
from ..database import conn
from ..worker import vaqt_uzgartirish
from eskiz_sms import EskizSMS
from fastapi_utils.tasks import repeat_every
email = "dilshodjon216@gmail.com"
password = "uaQbmdV41UnoSRFH43rzZOLtcry9HwTPVz9ToNoW"

eskiz = EskizSMS(email=email, password=password)
router = APIRouter(prefix="/mqtt", tags=["mqtt"])


mqtt_config = MQTTConfig(host= '185.196.214.190',
                         port= 1883,
                         username= "emqx",
                         password= "12345",
                         keepalive = 60)

mqtt = FastMQTT(
    config=mqtt_config
)

mqtt.init_app(router)

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    print("Connected: ", client, flags, rc, properties)

@mqtt.subscribe("W/+/+/+/data")
async def data_water( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.DataWaterInput(**json.loads(payload.decode()))
        data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
        conn.fastapi.data_water.insert_one(data_shcemas.dict())
    except Exception as e:
      pass

@mqtt.subscribe("M/+/+/+/data")
async def data_well( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.DataWellInput(**json.loads(payload.decode()))
        data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
        conn.fastapi.data_well.insert_one(data_shcemas.dict())
    except Exception as e:
      pass



async def info_water( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.StationInfoInput(**json.loads(payload.decode()))
        data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
        conn.fastapi.water_info.insert_one(data_shcemas.dict())
    except Exception as e:
      pass



async def info_well(client, topic, payload, qos, properties):
    try:
        data_shcemas = schemas.StationInfoInput(**json.loads(payload.decode()))
        data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
        conn.fastapi.well_info.insert_one(data_shcemas.dict())
    except Exception as e:
        pass

@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print(client, "Disconnected")
    print("Disconnected: ", client, packet, exc)