import paho.mqtt.client as mqtt
import json
from app import schemas
from app.database import conn
from app.worker import vaqt_uzgartirish


client = mqtt.Client()
client.connect('185.196.214.190', 1883)
client.username_pw_set(username="emqx", password="12345")


def on_connect(client, userdata, flags, rc):
    print("Connected to a data well!")
    client.subscribe("M/+/+/+/data")


def on_message(client, userdata, message):
    try:
        payload = message.payload.decode()
        data_shcemas = schemas.DataWellInput(**json.loads(payload))
        data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
        conn.fastapi.data_well.insert_one(data_shcemas.dict())
    except Exception as e:
      pass


client.on_connect = on_connect
client.on_message = on_message