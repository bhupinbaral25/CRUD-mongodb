import datetime
import os
from mongoengine import connect
import mongoengine_goodjson as gj
from mongoengine.fields import DateTimeField, StringField, EmailField

#  Read key-value pairs from a .env file and set them as environment variables
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database_name = os.environ.get("DATABASE_NAME")
host = os.environ["DB_HOST"]

# Connecting to MongoDB
host = f"mongodb+srv://{user}:{password}@{host}/{database_name}"
connect(host=host)

def not_null(name):
    if not name:
        raise ValueError("Name can not be empty")

class DefaultAttributes:
    meta = {"allow_inheritance": True}
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(DefaultAttributes, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        '''
        Take the  data as argument and added the modified date as attribute
        ------
        Return
        ------
        Return the object that save the updated data into the database 
        '''
        self.modified_date = datetime.datetime.now()
        return super(DefaultAttributes, self).save(*args, **kwargs)

class TODO(DefaultAttributes, gj.Document):
    """----------Basic class to define Payloads------------"""
    tittle = StringField(max_length=200, required=True)
    description = StringField(required=True)
    email = EmailField(required=True)
    phone = StringField(required=True)
    
