from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

from setting import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
