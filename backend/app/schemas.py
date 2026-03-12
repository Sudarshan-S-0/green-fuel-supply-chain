from pydantic import BaseModel

class FuelBatchCreate(BaseModel):
    batch_id: str
    fuel_type: str
    producer: str
    carbon_emission: str

class FuelBatchResponse(BaseModel):
    batch_id: str
    fuel_type: str
    producer: str
    carbon_emission: str
    status: str