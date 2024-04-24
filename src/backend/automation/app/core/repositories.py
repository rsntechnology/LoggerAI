from pymongo import MongoClient
from bson.objectid import ObjectId
from .entities import UseCase
from fastapi import HTTPException
import toml

class UseCaseRepository:
    def __init__(self):
        config = toml.load("config/config.toml")
        self.url = config["mongodb"]["url"]
        self.database_name = config["mongodb"]["database_name"]
        client = MongoClient(self.url)
        db = client["LoggerAI"]
        self.collection = db[self.database_name]

    def create_usecase(self, usecase: UseCase):
        if self.collection.find_one({"id": usecase.id}):
            raise HTTPException(status_code=404, detail="Use case ID must be unique.")
        self.collection.insert_one(usecase.__dict__)
        return usecase
    
    def get_usecase(self):
            return self.collection.find()
    
    def get_usecase(self, usecase_id: str):
        return self.collection.find_one({"id": (usecase_id)})

    def update_usecase(self, usecase_id: str, new_usecase: UseCase):
        print(new_usecase.__dict__, usecase_id)
        result = self.collection.update_one({"id": usecase_id}, {"$set": new_usecase.__dict__})
        if result.modified_count > 0:
            return self.get_usecase(usecase_id)
        return None

    def delete_usecase(self, usecase_id: str):
        result = self.collection.delete_one({"id": usecase_id})
        if result.deleted_count > 0:
            return usecase_id
        return None
