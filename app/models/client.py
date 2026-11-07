import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Enum
import enum
from app.core.database import Base



class ClientStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


# The client model
class Client(Base):
    __tablename__ = 'clients'

    id = Column(String, primary_key = True, default= lambda: str(uuid.uuid4()))
    company_name = Column(String, nullable= False)
    email = Column(String, unique= True, index= True, nullable= False)
    password = Column(String, nullable= False)

    contact_person = Column(String, nullable= False)
    phone_number = Column(String, nullable= False)

    status = Column(Enum(ClientStatus), default=ClientStatus.PENDING, nullable= False)

    created_at = Column(DateTime, default= lambda: datetime.now(), nullable= False)
    updated_at = Column(DateTime, default= lambda: datetime.now(), onupdate= lambda: datetime.now(), nullable= False)
