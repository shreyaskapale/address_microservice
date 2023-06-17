from typing import Optional
from pydantic import BaseModel, HttpUrl, Field

class AddressOutput(BaseModel):
    latitude: float
    longitude: float
    id:int