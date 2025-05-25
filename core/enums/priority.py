from enum import IntEnum

from core.enums import BaseEnum


class MessagePriority(BaseEnum):
    CRITICAL = 3
    IMPORTANT = 2
    NEUTRAL = 1


class Priority(BaseEnum, IntEnum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
