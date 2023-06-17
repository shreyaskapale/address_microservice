from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from repository.sqlite_connection import SqliteConnection
from repository.sqlite_connection import Base


class AddressDB(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)

def add_address_to_db(address, last):
    print(address)
    with SqliteConnection() as connection:
        session = connection
        new_address = AddressDB(latitude=address.latitude,longitude = address.longitude)
        session.add(new_address)
        if last:
            session.commit()
        session.refresh(new_address) 
        return new_address

def fetch_address_by_id_from_db(id):
    with SqliteConnection() as connection:
        session = connection
        return session.query(AddressDB).filter_by(id=id).first()
    
def fetch_all_addresses():
    addresses = []
    
    with SqliteConnection() as connection:
        session = connection
        fetched_products = session.query(AddressDB).all()
        for address in fetched_products:
            address_data = {
                "id": address.id,
                "latitude": address.latitude,
                "longitude": address.longitude,
            }
            addresses.append(address_data)

    return addresses

def update_address_by_id_from_db(address_id, new_latitude, new_longitude):
    with SqliteConnection() as connection:
        session = connection
        address = session.query(AddressDB).get(address_id)
        if address is None:
            return None  # Address with the given ID doesn't exist

        address.latitude = new_latitude
        address.longitude = new_longitude
        session.commit()

        session.refresh(address)
        return address


        
def delete_address_by_id_from_db(id):
    with SqliteConnection() as connection:
        session = connection
        address = session.query(AddressDB).filter_by(id=id).first()
        if address:
            session.delete(address)
            session.commit()
            return True
        else:
            return False