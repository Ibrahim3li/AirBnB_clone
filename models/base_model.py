#!usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())  # Assign a unique id using uuid4 and convert to string
        self.created_at = datetime.now()  # Assign current datetime when instance is created
        self.updated_at = datetime.now()  # Assign current datetime when instance is created

    def __str__(self):
        """Return the formatted string using format method"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

if __name__ == "__main__":
    """Create a new instance of BaseModel"""
    my_model = BaseModel()
    print(my_model)
