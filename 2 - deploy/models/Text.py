from pydantic import BaseModel


class Text(BaseModel):
    data = 'input the string'
