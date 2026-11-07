from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# lets just create an SQlite database for starting
SQLALCHEMY_DATABASE_URL = "sqlite:///./kotta.db"


# engine manages connectin to database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)



# Each API request will create its own temproary database session using this maker
# Auto commit = fasle ensures that transactions are controlled manually
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)


# Base class for database model
# All database models will inherit from this
Base = declarative_base()


# This function opens a databse session for a single database request and closes when its done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()