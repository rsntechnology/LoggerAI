from .repositories import UseCaseRepository
from .entities import UseCase

class UseCaseService:
    def __init__(self):
        self.repository = UseCaseRepository()

    def create_usecase(self, id: int, name: str, prompt: str, data_type: str, project: str, status: str, tags: dict):
        usecase = UseCase(id=id, name=name, prompt=prompt, data_type=data_type, project=project, status=status, tags=tags)
        return self.repository.create_usecase(usecase)
    
    def get_usecase_all(self):
        return self.repository.get_usecase_all()
    
    def get_usecase(self, usecase_id: int):
        return self.repository.get_usecase(usecase_id)

    def update_usecase(self, usecase_id: int, new_usecase: UseCase):
        return self.repository.update_usecase(usecase_id, new_usecase)

    def delete_usecase(self, usecase_id: int):
        return self.repository.delete_usecase(usecase_id)
