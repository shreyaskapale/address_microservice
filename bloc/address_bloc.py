from bloc.helpers import calculate_distance
from models.inputs.AddressInput import AddressInput
from models.outputs.AddressOutput import AddressOutput
from repository.native_address_repository import add_address_to_db, delete_address_by_id_from_db, fetch_address_by_id_from_db, fetch_all_addresses, update_address_by_id_from_db


def add_address(address):
    # Create a new AddressOutput object with the provided latitude and longitude
    new_address = AddressOutput(id=0, longitude=address.longitude, latitude=address.latitude)
    
    # Add the new address to the database
    return add_address_to_db(new_address, True)

def update_address(id, address):
    # Update the address in the database with the provided latitude and longitude
    return update_address_by_id_from_db(id, address.latitude, address.longitude)

def get_address_by_id(id):
    # Fetch the address from the database by its ID
    return fetch_address_by_id_from_db(id)

def delete_address(id):
    # Delete the address from the database by its ID
    return delete_address_by_id_from_db(id)

def nearby_distance(inputAddress: AddressInput, distance, distanceType):
    # Fetch all addresses from the database
    all_addresses = fetch_all_addresses()
    
    # Initialize an empty list to store nearby addresses
    addresses = []
    
    # Iterate over each address
    for address in all_addresses:
        # Calculate the distance between the input address and the current address
        calculated_distance = calculate_distance(inputAddress.latitude, inputAddress.longitude, address['latitude'], address['longitude'], distanceType)
        
        # Check if the calculated distance is less than the specified distance
        if distance > calculated_distance:
            # Add the address to the list of nearby addresses
            addresses.append(address)
    
    # Return the list of nearby addresses
    return addresses
