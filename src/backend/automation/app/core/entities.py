from typing import List
from pydantic import BaseModel

class UseCase(BaseModel):
    id: int
    name: str
    prompt: str
    data_type: str
    project: str
    status: str
    tags: List[str]

class CreateUseCaseRequest(BaseModel):
    id: int
    name: str
    prompt: str
    data_type: str
    project: str
    status: str
    tags: List[str]
