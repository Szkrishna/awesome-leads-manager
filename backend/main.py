import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI()

@app.post("/api/create-user")
async def create_user(user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="email alredy in use")
    
    return await _services.create_user(user, db)


@app.get("/api/user-list")
async def get_users(db: _orm.Session = _fastapi.Depends(_services.get_db)):    
    db_users = await  _services.get_users(db)
    return db_users


@app.get("/api/test")
async def test():    
    return {"message":"Api working...."}