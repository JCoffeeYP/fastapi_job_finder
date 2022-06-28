from typing import Generator

import sqlalchemy.orm
from config.settings import settings

engine = sqlalchemy.create_engine(settings.POSTGRES_DSN, pool_pre_ping=True)

SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

