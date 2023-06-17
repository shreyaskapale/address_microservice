
# Address Microservice

This is an API for managing addresses using FastAPI.

## Folder Structure
    /apis/ versioning - where apis are defined 
    /repository - for SQLalchemy ORM for Address for db transactions
    /bloc - business logic layer, where logic level processing takes place
    /enums - for types KM / Miles for distance based address fetching
    /errors - for defining errors for api
    /middleware - for defining auth and logging
    /models - for storing pydantic models for address
    /models/input - for defining models which are for api inputs
    /modles/output -for defining models which are for response outputs from api
    

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/address-bloc-api.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Start the server:

```bash
uvicorn app:app --reload
```

The API will be accessible at `http://localhost:8000`.

Swagger DOCS will be accessible at `http://localhost:8000/docs`.


## API Endpoints

### Create a New Address

- **URL:** `/address`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "latitude": 40.7128,
      "longitude": -74.0060
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "latitude": 40.7128,
      "longitude": -74.0060
    }
    ```

### Update an Existing Address

- **URL:** `/address`
- **Method:** `PATCH`
- **Query Parameters:**
  - `id` (integer, required) - The ID of the address to update
- **Request Body:**
    ```json
    {
      "latitude": 40.7128,
      "longitude": -74.0060
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "latitude": 40.7128,
      "longitude": -74.0060
    }
    ```

### Retrieve an Address by ID

- **URL:** `/address`
- **Method:** `GET`
- **Query Parameters:**
  - `id` (integer, required) - The ID of the address to retrieve
- **Response:**
    ```json
    {
      "id": 1,
      "latitude": 40.7128,
      "longitude": -74.0060
    }
    ```

### Delete an Address by ID

- **URL:** `/address`
- **Method:** `DELETE`
- **Query Parameters:**
  - `id` (integer, required) - The ID of the address to delete
- **Response:**
    ```json
    {
      "message": "Address deleted successfully"
    }
    ```

### Retrieve Nearby Addresses

- **URL:** `/nearby`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "latitude": 40.7128,
      "longitude": -74.0060
    }
    ```
- **Query Parameters:**
  - `distance` (float, required) - The distance in meters
  - `distanceType` (string, required) - The type of distance ("km" or "miles")
- **Response:**
    ```json
    {
      "nearby_addresses": [
        {
          "id": 1,
          "latitude": 40.7128,
          "longitude": -74.0060
        },
        {
          "id": 2,
          "latitude": 40.7306,
          "longitude": -73.9352
        }
      ]
    }
    ```

## Error Handling

- `ItemNotFound` (404 Not Found): Raised when an address with the specified ID is not found.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

