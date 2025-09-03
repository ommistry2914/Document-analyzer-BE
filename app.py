from fastapi import FastAPI, APIRouter
from routes import auth_routes, doc_routes
from fastapi.middleware.cors import CORSMiddleware
import os
from config import UPLOAD_DIR, INDEX_DIR

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)

app = FastAPI(title="Document Q&A Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"status": "ok", "message": "Server is running"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running"}



@app.on_event("startup")
async def startup_event():
    print("🚀 Server is up and running.")

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(auth_routes.router)
# app.include_router(doc_routes.router)


app.include_router(v1_router)