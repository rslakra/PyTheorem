from enum import auto, IntEnum
from core.enums import BaseEnum

class LogTypeEnum(BaseEnum, IntEnum):
    """LogTypeEnum defines various log levels. For readability, add constants in Alphabetical order."""
    ALL = auto()
    DEBUG = auto()
    INFO = auto()
    WARN = auto()
    ERROR = auto()
