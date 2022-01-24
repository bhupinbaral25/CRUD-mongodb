import re
import pydantic
import bson
from typing import Optional
class ValidateCreateTODOModel(pydantic.BaseModel):
    tittle:str
    description:str
    email: str
    phone: str

    @pydantic.validator("email")
    @classmethod
    def email_valid_check(cls, email: str) -> str:
        '''
        Email checked using regular expression
        '''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            message = f"Given email address ({email}) is invalid."
            raise ValueError(message=message)

    @pydantic.validator("phone")
    @classmethod
    def phone_valid_check(cls, phone: str) -> str:
       
        regex = r'^(?:[+977]9)?[0-9]{10}$'
        if(re.fullmatch(regex, phone)):
            return phone
        else:
            message = f"Given phone number ({phone}) is not valid."
            raise ValueError(message=message)

class ValidateDeleteModel(pydantic.BaseModel):
    id: str

    @pydantic.validator("id")
    @classmethod
    def id_valid_check(cls, id) -> None:
        #* Check mongo ObjectID is valid.
        if bson.objectid.ObjectId.is_valid(id):
            return id
        else:
            message = f"Given id ({id}) is not valid object id."
            raise ValueError(message=message)

class ValidateUpdateModel(pydantic.BaseModel):
    id: str
    tittle: str
    description: str
    email: Optional[str]
    phone: Optional[str]
    
    @pydantic.validator("email")
    @classmethod
    def email_valid_check(cls, email) -> None:
        #* Make a regular expression for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            message = f"Given email address ({email}) is invalid."
            raise ValueError(message=message)

    @pydantic.validator("phone")
    @classmethod
    def phone_valid_check(cls, phone) -> None:
        #* Make a regular expression for validating Phone Number
        regex = r'^(?:[+977]9)?[0-9]{10}$'
        if(re.fullmatch(regex, phone)):
            return phone
        else:
            message = f"Given phone number ({phone}) is invalid."
            raise ValueError(message=message)

    @pydantic.validator("id")
    @classmethod
    def id_valid_check(cls, id) -> None:
        #* Check mongo ObjectID is valid.
        if bson.objectid.ObjectId.is_valid(id):
            return id
        else:
            message = f"Given id ({id}) is not valid object id in update operation."
            raise ValueError( message=message)

