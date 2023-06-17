from fastapi import  HTTPException
ItemNotFound = HTTPException(status_code=404, detail="Item not found")