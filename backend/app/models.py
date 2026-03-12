from sqlalchemy import Column, Integer, String
from .database import Base

class FuelBatch(Base):
    __tablename__ = "fuel_batches"

    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(String, unique=True)
    fuel_type = Column(String)
    producer = Column(String)
    carbon_emission = Column(String)
    status = Column(String)