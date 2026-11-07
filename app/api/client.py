from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import hash_password
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientResponse


# API router for client routes
router = APIRouter(prefix="/clients", tags= ["Clients"])


@router.post("/register", response_model = ClientResponse, status_code= status.HTTP_201_CREATED)
def register_client(client_in: ClientCreate, db: Session = Depends(get_db)):


    # Check if the email exists
    existing_client = db.query(Client).filter(Client.email == client_in.email).first()
    if existing_client:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "An account with same email already exists."
        )

    hashed_pwd= hash_password(client_in.password)

    # Create new client
    new_client= Client(
        company_name = client_in.company_name,
        email= client_in.email,
        password= hashed_pwd,
        contact_person= client_in.contact_person,
        phone_number= client_in.phone_number
    )


    # commit 
    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    # Return the model
    return new_client