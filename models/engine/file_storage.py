# #!usr/bin/python3
# """file storage module"""
# import json 
# import os

# class FileStorage:
#     __file_path = "file.json"
#     __objects = {}

# def all(self):
#     """returns the dictionary __objects"""
#     return self.__objects
# def new(self, obj):
#     """sets in __objects the obj with key <obj class name>.id"""
#     key = "{}.{}".format(type(obj).__name__, obj.id)
#     self.__objects[key] = obj

# def save(self):
#     """serializes __objects to the json file (path: __file_path)."""
#     obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
#     with open(self.__file_path, 'w') as file:
#         json.dump(obj_dict, file)

#     def reolad(self):
#         """deserializes the json file to __objects (only if the json file (__file_path) exists, otherwise do nothing)"""
#         if os.path.exists(self.__file_path):
#             with open (self.__file_path):
#                 obj_dict = json.load(file)
#                 for key, value in obj_dict.items():
#                     class_name = value['__class__']
#                     cls = globals()[class_name]
#                     self.__objects[key] = cls (**value)

class Student():
    def __init__(self, name):
        self.name = name

students = []
s = Student("John")
students.append(s)
print(students)