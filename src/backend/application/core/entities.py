from pydantic import BaseModel

class Loger(BaseModel):
    message: dict

class Metric(BaseModel):
    message: dict

class Error(BaseModel):
    message: dict