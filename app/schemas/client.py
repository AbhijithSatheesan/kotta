from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.client import ClientStatus

# This is schema for inputs
class ClientCreate(BaseModel):
    company_name : str
    email : EmailStr
    password : str
    contact_person : str
    phone_number : str


class ClientResponse(BaseModel):
    id : str
    company_name : str
    email : EmailStr
    contact_person : str
    phone_number : str
    status : ClientStatus

    # To allow pydantic to read data directly from sqlalchemy models
    class  Config:
        from_attributes = True
