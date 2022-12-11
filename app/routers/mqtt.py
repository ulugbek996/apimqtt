from fastapi import FastAPI , APIRouter
from fastapi_mqtt import FastMQTT, MQTTConfig
from .. import models,schemas
import json
from ..database import conn
from ..worker import vaqt_uzgartirish
from eskiz_sms import EskizSMS

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
    mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@mqtt.subscribe("W/+/+/+/data")
async def data_water( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.DataWaterInput(**json.loads(payload.decode()))
        conn.fastapi.data_water.insert_one(data_shcemas.dict())
    except Exception as e:
      pass

@mqtt.subscribe("M/+/+/+/data")
async def data_well( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.DataWellInput(**json.loads(payload.decode()))
        conn.fastapi.data_well.insert_one(data_shcemas.dict())
    except Exception as e:
      pass

@mqtt.subscribe("W/+/+/+/info")
async def info_water( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.StationInfoInput(**json.loads(payload.decode()))
        conn.fastapi.water_info.insert_one(data_shcemas.dict())
    except Exception as e:
      pass
@mqtt.subscribe("W/send/sms")
async def send_sms( client, topic, payload, qos, properties ):
    try:
        data = payload.decode()
        data_shemas = schemas.Alert2(**json.loads(data))
        data_shemas.time = vaqt_uzgartirish(data_shemas.time)
        send_text = f"Sizning: {data_shemas.name} nomli kanaldagi qurilma soat {data_shemas.time}da qo'zg'aldi taxminiy joylashih {data_shemas.locatsiya} ehtiyot bo'ling yo'qolishi mumkin"
        eskiz.send_sms('998998429684',send_text, from_whom = '4546', callback_url = None)
    except Exception as e:
      print(e)

@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)