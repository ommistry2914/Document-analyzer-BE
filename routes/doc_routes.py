# from fastapi import APIRouter, UploadFile, File, Form, HTTPException
# from database import documents_collection, sessions_collection
# from services.llama_service import build_index, load_index, query_index
# import os
# from bson import ObjectId
# from config import UPLOAD_DIR, INDEX_DIR
# from utils.security import decode_access_token

# router = APIRouter(prefix="/docs")

# # Auth dependency
# def get_current_user(token: str = Form(...)):
#     payload = decode_access_token(token)
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return payload["user_id"]

# # Upload document
# @router.post("/upload")
# async def upload_document(file: UploadFile = File(...), token: str = Form(...)):
#     user_id = get_current_user(token)
#     user_dir = os.path.join(UPLOAD_DIR, user_id)
#     os.makedirs(user_dir, exist_ok=True)
#     file_path = os.path.join(user_dir, file.filename)

#     with open(file_path, "wb") as f:
#         f.write(await file.read())

#     # Build index
#     index_dir = os.path.join(INDEX_DIR, user_id)
#     os.makedirs(index_dir, exist_ok=True)
#     index_path = os.path.join(index_dir, f"{file.filename}.json")
#     build_index(file_path, index_path)

#     doc_data = {
#         "filename": file.filename,
#         "filepath": file_path,
#         "indexpath": index_path,
#         "user_id": user_id
#     }
#     await documents_collection.insert_one(doc_data)
#     return {"message": "Document uploaded and indexed"}

# # List user's documents
# @router.get("/list")
# async def list_docs(token: str):
#     user_id = get_current_user(token)
#     docs = await documents_collection.find({"user_id": user_id}).to_list(length=100)
#     return docs

# # Query / chat
# @router.post("/query")
# async def chat_query(
#     token: str = Form(...),
#     document_id: str = Form(...),
#     query: str = Form(...),
#     model: str = Form(...)
# ):
#     user_id = get_current_user(token)
#     doc = await documents_collection.find_one({"_id": ObjectId(document_id), "user_id": user_id})
#     if not doc:
#         raise HTTPException(status_code=404, detail="Document not found")

#     index = load_index(doc["indexpath"])
#     answer = query_index(index, query, model)

#     # Save chat session
#     await sessions_collection.update_one(
#         {"user_id": user_id},
#         {"$push": {"chats": {"document_id": document_id, "query": query, "answer": answer, "model": model}}},
#         upsert=True
#     )
#     return {"answer": answer}
