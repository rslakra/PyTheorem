# Python Enums
# Author: Rohtash Lakra
# Reference - https://docs.python.org/3/howto/enum.html
#
import sys

from enum import unique, auto

from core.enums import AutoNameEnum

print()
print(f"Sys Version: {sys.version_info}")
print()
# String Enum
if sys.version_info >= (3, 11):
    from enum import StrEnum
    # from strenum import StrEnum
    class HttpMethodEnum(StrEnum):
        """HttpMethod enums defines supported http methods. For readability, add constants in Alphabetical order."""
        GET = auto()
        HEAD = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
        CONNECT = auto()
        OPTIONS = auto()
        TRACE = auto()
        PATCH = auto()
else:
    @unique
    class HttpMethodEnum(AutoNameEnum):
        """HttpMethod enums defines supported http methods. For readability, add constants in Alphabetical order."""
        CONNECT = auto()
        HEAD = auto()
        GET = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
        OPTIONS = auto()
        TRACE = auto()
        PATCH = auto()

        """
        _missing_(cls, value)
        A 'classmethod' for looking up values not found in cls. 
        By default it does nothing, but can be overridden to implement custom search behavior:
        """

        @classmethod
        def _missing_(cls, value):
            value = value.upper()
            for member in cls:
                if member.value == value:
                    return member

            return None
