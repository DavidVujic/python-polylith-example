from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sql_app.db"
DATABASE_ARGS = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=DATABASE_ARGS)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)
