from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# Generate Database URL
DATABASE_URL = 'sqlite:///./user_api.db'

# Create Database Engine
Engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
