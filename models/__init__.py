#!/usr/bin/python3
"""This module contains the init file for the models package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
