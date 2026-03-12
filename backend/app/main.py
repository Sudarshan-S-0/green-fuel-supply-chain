from fastapi import FastAPI
from .database import engine
from . import models
from .routes import fuel_routes
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Green Energy Supply Chain API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fuel_routes.router)

@app.get("/")
def home():
    return {"message": "Green Energy Supply Chain Backend Running"}