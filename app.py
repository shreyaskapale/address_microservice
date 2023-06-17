from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.v1.address import router as address_v1
from middleware.logging_middleware import logging_middleware
from repository.sqlite_connection import SqliteConnection

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# auth middle ware can be added here 
# app.middleware("http")(auth_middleware)
app.middleware("http")(logging_middleware)

app.include_router(address_v1, prefix="/v1/users")