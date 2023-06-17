from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse

async def logging_middleware(request: Request, call_next): 
    # Implement logging logic here 
    response = await call_next(request) 
    return response