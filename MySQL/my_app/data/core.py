# from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from urllib.parse import quote_plus
# load_dotenv()

""" You can add a DATABASE_URL environment variable to your .env file """
# DATABASE_URL = os.getenv("DATABASE_URL")

""" Or hard code PostgreSQL here """
DATABASE_URL="mysql+pymysql://root:%s@localhost:3306/fastapi_poc"

engine = create_engine(DATABASE_URL % quote_plus("Admin@12345"))

SessionLocal = sessionmaker(autocommit=False, bind=engine)

class DbBase(DeclarativeBase):
    pass


def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
        db_session.commit()
    except Exception:
        db_session.rollback()
        raise
    finally:
        db_session.close()
        


