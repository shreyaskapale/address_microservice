from fastapi import APIRouter
from bloc.address_bloc import add_address, delete_address, get_address_by_id, nearby_distance, update_address
from enums.DistanceType import DistanceType
from errors.ItemNotFound import ItemNotFound

from models.inputs.AddressInput import AddressInput

router = APIRouter()

# API endpoint to create a new address
@router.post("/address")
async def post_address_api(addressInput: AddressInput):
    return add_address(address=addressInput)


# API endpoint to update an existing address
@router.patch("/address")
async def update_address_api(id: int, addressInput: AddressInput):
    result = update_address(id, addressInput)
    if result is None:
        raise ItemNotFound  # Raise an exception if the address is not found
    return result


# API endpoint to retrieve an address by ID
@router.get("/address")
async def get_address_api(id: int):
    result = get_address_by_id(id)
    if result is None:
        raise ItemNotFound  # Raise an exception if the address is not found
    return result


# API endpoint to delete an address by ID
@router.delete("/address")
async def delete_address_api(id: int):
    return delete_address(id)


# API endpoint to retrieve nearby addresses within a certain distance
@router.post("/nearby")
async def get_nearby_api(address: AddressInput, distance: float, distanceType: DistanceType):
    result = nearby_distance(address, distance, distanceType)
    return result
