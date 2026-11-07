from fastapi import FastAPI
from app.api.client import router as client_router
from app.core.database import engine, Base


# Create tables in SQLite (for development setup)
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(client_router)

@app.get("/")
def read_root():
    return {"status" : "online", "message" : "API is running"}