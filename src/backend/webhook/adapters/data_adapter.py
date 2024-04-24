from fastapi import APIRouter, HTTPException, Query
from application.ports.data_ports import DataPort
from application.core.repositories import DataRepository
from typing import List
import toml

config = toml.load("config/config.toml")

router = APIRouter()

@router.get("/{data_type}/{application}")
async def retrieve_data(data_type: str, application: str, start_date: str = Query(None), end_date: str = Query(None)):
    # Retrieve data from the DataRepository
    path = f"{config['base_path']['name']}/{application}"
    # Create an instance of the DataRepository with the appropriate data directory path
    data_repository = DataRepository(data_directory=path)  # Provide the correct data directory path
    data = data_repository.retrieve_data(data_type, application, start_date, end_date)
    if "code" in data:
        raise HTTPException(status_code=404, detail=data["error"])
    flat_data = []

    # Iterate through the nested lists
    for inner_list in data:
        # Iterate through the dictionaries in each inner list
        for inner_dict in inner_list:
            # Append the message dictionary to the flat_data list
            flat_data.append(inner_dict['message'])

    # Return the flattened data as a list
    return flat_data
