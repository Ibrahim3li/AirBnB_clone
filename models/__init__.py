#!usr/bin/python3
"""the init for package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
