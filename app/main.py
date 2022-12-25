from fastapi import FastAPI
from .database import engine
from . import models, datawell , datawater ,infowell ,infowater
from .routers  import  mqtt ,tasks ,stationinfo ,user ,auth , station ,data ,info ,datetime
from . schemas import Task , WellSorting , WaterSorting

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
datawell.client.loop_start()
datawater.client.loop_start()
infowell.client.loop_start()
infowater.client.loop_start()
#app.include_router(mqtt.router)
app.include_router(tasks.router)
app.include_router(stationinfo.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(station.router)
app.include_router(data.router)
app.include_router(info.router)
#app.include_router(datetime.router)

@app.get("/")
def root():
    return {"message": "Hello World"}



@app.post("/task")
async def create(task: Task):
    return task.save()

@app.post('/watersorting')
async def water_sorting(sorting: WaterSorting):
    return sorting.save()

@app.post("/wellsorting")
async def well_sorting(sorting: WellSorting):
    return sorting.save()

@app.get("/tasks")
async def all():
    return [format(pk) for pk in Task.all_pks()]

def format(pk:str):
    task = Task.get(pk)
    return {
        "id":task.pk,
        "name": task.name,
        "description": task.description
    }
