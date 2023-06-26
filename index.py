from fastapi import FastAPI
import uvicorn
from routes.user import user_router

app = FastAPI()
app.include_router(user_router)
uvicorn.run(app, host="0.0.0.0", port=8000)
