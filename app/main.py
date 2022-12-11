from fastapi import FastAPI
from .database import engine
from . import models
from .routers  import  mqtt ,tasks ,stationinfo ,user ,auth , station


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(mqtt.router)
app.include_router(tasks.router)
app.include_router(stationinfo.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(station.router)


@app.get("/")
def get_station_info():
    return {"message": "Hello World"}


