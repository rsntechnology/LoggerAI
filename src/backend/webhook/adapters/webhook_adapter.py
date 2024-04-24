from fastapi import APIRouter
from application.core.entities import Loger, Metric, Error
from application.core.use_case import ProcessWebhookUseCase
from application.core.repositories import DataRepository
import os, json
from fastapi import APIRouter, BackgroundTasks
from application.core.entities import Loger, Metric, Error
from application.core.use_case import ProcessWebhookUseCase
from application.core.repositories import DataRepository
import os, json
import toml

config = toml.load("config/config.toml")
router = APIRouter()

router = APIRouter()

@router.post("/")
async def process_webhook(data: dict, background_tasks: BackgroundTasks):
    data =(json.dumps(data))
    data = json.loads(data)
    # Initialize use case with appropriate dependencies
    application = data["application"]
    # Ensure directory exists before writing files
    directory = f"{config['base_path']['name']}/{application}"
    if not os.path.exists(directory):
        os.makedirs(directory)   
    data_repository = DataRepository(data_directory=directory)  # Provide the correct data directory path
    use_case = ProcessWebhookUseCase(data_repository=data_repository)

    # Queue the execution of the use case
    background_tasks.add_task(use_case.execute, data)

    return {"message": "Webhook queued for processing"}
