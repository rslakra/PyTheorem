from core.enums import BaseEnum

# Python Enums
# Author: Rohtash Lakra
# Reference - https://docs.python.org/3/howto/enum.html
#

from enum import auto, IntFlag


# In cases where the actual values of the members do not matter,
# you can save yourself some work and use auto() for the values:
class NumberEnum(BaseEnum):
    """Number types Enum. For readability, add constants in Alphabetical order."""
    EVEN = auto()
    ODD = auto()
    PRIME = auto()


class EvenOddEnum(BaseEnum, IntFlag):
    """EvenOddEnum defines even and odd enums. For readability, add constants in Alphabetical order."""

    EVEN = auto()
    ODD = auto()
