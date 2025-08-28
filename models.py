from pydantic import BaseModel

class Notifications(BaseModel):
    Type: str
    Name: str
    Description: str