from fastapi import APIRouter, Depends, HTTPException
from app.core.services import UseCaseService
from app.core.entities import CreateUseCaseRequest
from typing import Any
from bson import json_util
import json
router = APIRouter(prefix="/usecases")

@router.post("/", response_model= Any)
def create_usecase(usecase: CreateUseCaseRequest):
    usecase_service = UseCaseService()
    created_usecase = usecase_service.create_usecase(usecase.id,usecase.name, usecase.prompt, usecase.data_type, usecase.project, usecase.status, usecase.tags)
    return created_usecase

@router.get("/", response_model=Any)
def get_usecase():
    usecase_service = UseCaseService()
    usecase = usecase_service.get_usecase_all()
    if not usecase:
        raise HTTPException(status_code=404, detail="Use case not found")
    return json.loads(json_util.dumps(usecase))

@router.get("/{usecase_id}", response_model=Any)
def get_usecase(usecase_id: int):
    usecase_service = UseCaseService()
    usecase = usecase_service.get_usecase(usecase_id)
    if not usecase:
        raise HTTPException(status_code=404, detail="Use case not found")
    return json.loads(json_util.dumps(usecase))

@router.put("/{usecase_id}", response_model=Any)
def update_usecase(usecase_id: int, usecase: CreateUseCaseRequest):
    usecase_service = UseCaseService()
    updated_usecase = usecase_service.update_usecase(usecase_id, usecase)
    if not updated_usecase:
        raise HTTPException(status_code=404, detail="Use case not found")
    return json.loads(json_util.dumps(updated_usecase))

@router.delete("/{usecase_id}", response_model=Any)
def delete_usecase(usecase_id: int):
    usecase_service = UseCaseService()
    deleted_usecase = usecase_service.delete_usecase(usecase_id)
    if not deleted_usecase:
        raise HTTPException(status_code=404, detail="Use case not found")
    return deleted_usecase
