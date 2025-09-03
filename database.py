from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["document_qa_db"]
users_collection = db["users"]
documents_collection = db["documents"]
sessions_collection = db["sessions"]
