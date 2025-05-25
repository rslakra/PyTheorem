from enum import auto

from core.enums import AutoNameEnum, AutoNameLowerCaseEnum


# Ordinal Enum
class OrdinalEnum(AutoNameEnum):
    """OrdinalEnum defines all 4 ordinals. For readability, add constants in Alphabetical order."""

    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()


# LowerCase Ordinal Enum
class LowerCaseOrdinalEnum(AutoNameLowerCaseEnum):
    """LowerCaseOrdinalEnum defines all 4 ordinals in lowercase. For readability, add constants in Alphabetical order."""

    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
