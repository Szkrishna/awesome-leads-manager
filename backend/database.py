import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as _orm

# Database connection URL
DATABASE_URL = "sqlite:///./database.db"

# Creating the database engine
engine = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Creating a session factory
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
