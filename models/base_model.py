import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())  # Generate a unique id and convert to string
        self.created_at = datetime.now()  # Set created_at to current datetime
        self.updated_at = datetime.now()  # Set updated_at to current datetime

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        # Create a copy of the instance's __dict__ to avoid modifying the original
        instance_dict = self.__dict__.copy()

        # Add a key __class__ with the class name
        instance_dict['__class__'] = type(self).__name__

        # Convert created_at and updated_at to string in ISO format
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict

if __name__ == "__main__":
    # Create a new instance of BaseModel
    my_model = BaseModel()
    # Print the instance, which calls the __str__ method
    print(my_model)
    # Save the instance, updating the updated_at attribute
    my_model.save()
    # Print the instance dictionary representation
    print(my_model.to_dict())
