from enum import auto

from core.enums import BaseEnum


# Using automatic values
class StatusEnum(BaseEnum):
    """Status Enum defines various statuses. For readability, add constants in Alphabetical order."""

    # The values are chosen by _generate_next_value_() static, which can be overridden:
    # Note The _generate_next_value_() method must be defined before any members.
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    ENABLED = auto()
    DISABLED = auto()
    MODIFIED = auto()
    DELETED = auto()

    """
    _missing_(cls, value)
    A 'classmethod' for looking up values not found in cls. 
    By default it does nothing, but can be overridden to implement custom search behavior:
    """

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member

        return None
