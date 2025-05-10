import os
from sqlmodel import SQLModel, create_engine, Session

# Get the database URL from environment
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://buddie:buddie@localhost:5432/buddie")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """Create database tables from SQLModel models."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency for getting DB session."""
    with Session(engine) as session:
        yield session 