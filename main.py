from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models import UserRegister, Token
from auth import authenticate_user, create_access_token, get_current_user
from utils import fake_db, hash_password
from uuid import uuid4

app = FastAPI()


@app.post("/register")
def register(user: UserRegister):
    if user.email in fake_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    user_id = str(uuid4())
    fake_db[user.email] = {
        "id": user_id,
        "email": user.email,
        "password": hash_password(user.password) 
    }
    
    return {"id": user_id, "email": user.email}


@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token(data={"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/public-data")
def public_data():
    return {"message": "This is public data, no authentication needed."}


@app.get("/private-data")
def private_data(current_user: dict = Depends(get_current_user)):
    return {"message": f"This is protected data for {current_user['email']}"}
