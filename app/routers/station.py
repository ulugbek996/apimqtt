from fastapi import FastAPI , APIRouter ,Depends
from sqlalchemy.orm import Session, lazyload
from ..database import get_db
from .. import models, schemas ,oauth2


router = APIRouter(prefix="/station", tags=["Station"])

@router.post('/create')
def create_station(station: schemas.WaterStationCreate, db: Session = Depends(get_db)):
    new_station = models.WaterStation(**station.dict())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return new_station