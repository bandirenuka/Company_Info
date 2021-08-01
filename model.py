from pydantic import BaseModel

class Company(BaseModel):
    name:str
    address:str
    owner_info:str
    employee_size: int

