#!/usr/bin/python3
"""Module for FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            serialized_objs = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(serialized_objs, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objs = json.load(file)
                for key, obj_dict in loaded_objs.items():
                    class_name = obj_dict.pop('__class__')
                    module_name = class_name.lower()
                    module = __import__('models.' + module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            serialized_objs = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(serialized_objs, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objs = json.load(file)
                for key, obj_dict in loaded_objs.items():
                    class_name = obj_dict.pop('__class__')
                    module_name = class_name.lower()
                    module = __import__('models.' + module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
