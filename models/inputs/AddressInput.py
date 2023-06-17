from typing import Optional
from pydantic import BaseModel, HttpUrl, Field

class AddressInput(BaseModel):
    latitude: float
    longitude: float