import sqlalchemy as _sql
from sqlalchemy.ext.declarative import _declerative
import sqlalchemy.orm as _orm


DATABASE_URL = "sqlite:///./databse.db"

engine = _sql.create_engine(DATABASE_URL), connect_args={"check_same_thred": False}

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declerative.declerative_base()