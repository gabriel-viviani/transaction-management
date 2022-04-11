from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from datetime import datetime
import uuid
import pytz

DEFAULT_TIMEZONE_REGION = "America/Sao_Paulo"

engine = create_engine("sqlite:///app.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()


def generate_uuid():
    return str(uuid.uuid4())


def gen_now() -> datetime:
    tz = pytz.timezone(DEFAULT_TIMEZONE_REGION)
    return datetime.now(tz)


def init_db() -> None:
    Base.metadata.create_all(engine)
    return
