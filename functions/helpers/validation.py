import re
import pydantic

class ValidationError(Exception):
    """Custom error that is raised when validation fail."""

    def __init__(self,value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class TODOModel(pydantic.BaseModel):
    tittle:str
    description:str

    @pydantic.validator("email")
    @classmethod
    def email_valid_check(cls, email) -> None:
        #* Make a regular expression for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            message = f"Given email address ({email}) is not valid."
            raise ValidationError(value=email, message=message)

    @pydantic.validator("phone")
    @classmethod
    def phone_valid_check(cls, phone) -> None:
        #* Make a regular expression for validating Phone Number
        regex = r'^(?:[+977]9)?[0-9]{10}$'
        if(re.fullmatch(regex, phone)):
            return phone
        else:
            message = f"Given phone number ({phone}) is not valid."
            raise ValidationError(value=phone, message=message)
