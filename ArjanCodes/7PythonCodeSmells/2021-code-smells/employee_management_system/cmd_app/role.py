"""Roles to clasify the type of employee"""
from enum import Enum, auto

class Role(Enum):
    """Employee roles types"""
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()
