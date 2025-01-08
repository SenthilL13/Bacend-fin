from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys
import uvicorn
from app import route

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
# load_dotenv(env_path)
sys.path.append(str(Path(__file__).absolute().parents[1]))

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"Server": "In live"}


@app.post("/FINO_ChatBot/login")
async def login(request: Request):
    try:
        if request:
            json_data = await request.json()
            response = route.ch_login(json_data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in login" + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/FINO_ChatBot/chat_assist")
async def chat_assist(request: Request):
    try:
        if request:
            json_data = await request.json()
            response = route.ch_chat_assist(json_data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in chat_assist" + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/FINO_ChatBot/signup")
async def signup(request: Request):
    try:
        if request:
            json_data = await request.json()
            response = route.ch_signup(json_data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in signup" + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/FINO_ChatBot/services_management")
async def services_management(request: Request):
    try:
        if request:
            json_data = await request.json()
            response = route.ch_services_management(json_data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in services_management: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/FINO_ChatBot/user_management")
async def user_management(request: Request):
    try:
        if request:
            json_data = await request.json()
            response = route.ch_user_management(json_data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_management: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
