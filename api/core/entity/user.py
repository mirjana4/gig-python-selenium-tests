from typing import Dict
from schema import And, Or, Regex


class User:
    id: int
    name: str
    email: str
    gender: str
    status: str

    def __init__(self, id, name, email, gender, status):
        self.id = id
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def from_json(data: Dict):
        return User(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            gender=data['gender'],
            status=data['status']
        )

    @staticmethod
    def json_schema() -> Dict:
        return {
            'id': int,
            'name': And(str, len),
            'email': And(str, Regex(r'^\S+@\S+\.\S+$')),
            'gender': And(str, Or('male', 'female')),
            'status': And(str, Or('active', 'inactive'))
        }
