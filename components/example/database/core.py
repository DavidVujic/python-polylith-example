from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./sql_app.db"
DATABASE_ARGS = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=DATABASE_ARGS)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
