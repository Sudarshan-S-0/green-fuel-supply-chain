from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from ..blockchain.web3_service import add_batch_to_blockchain

router = APIRouter()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Add new fuel batch
@router.post("/add-batch")
def add_batch(batch: schemas.FuelBatchCreate, db: Session = Depends(get_db)):
    existing = db.query(models.FuelBatch).filter(
        models.FuelBatch.batch_id == batch.batch_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Batch ID already exists")
    # Save to database
    new_batch = models.FuelBatch(
        batch_id=batch.batch_id,
        fuel_type=batch.fuel_type,
        producer=batch.producer,
        carbon_emission=batch.carbon_emission,
        status="Producer"
    )

    db.add(new_batch)
    db.commit()
    db.refresh(new_batch)

    # Send batch to blockchain
    tx_hash = add_batch_to_blockchain(batch.batch_id)

    return {
        "message": "Fuel batch added successfully",
        "blockchain_tx": tx_hash
    }


# Track fuel batch
@router.get("/track-batch/{batch_id}")
def track_batch(batch_id: str, db: Session = Depends(get_db)):

    batch = db.query(models.FuelBatch).filter(
        models.FuelBatch.batch_id == batch_id
    ).first()

    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")

    return {
        "batch_id": batch.batch_id,
        "fuel_type": batch.fuel_type,
        "producer": batch.producer,
        "carbon_emission": batch.carbon_emission,
        "status": batch.status
    }


# Update supply chain stage
@router.put("/update-stage/{batch_id}")
def update_stage(batch_id: str, new_stage: str, db: Session = Depends(get_db)):

    batch = db.query(models.FuelBatch).filter(
        models.FuelBatch.batch_id == batch_id
    ).first()

    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")

    batch.status = new_stage
    db.commit()

    return {"message": f"Batch moved to stage: {new_stage}"}