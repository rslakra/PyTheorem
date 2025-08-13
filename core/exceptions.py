#
# Author: Rohtash Lakra
#
"""
This module defines custom HTTP exceptions that include:
- HttpException: Base class for all custom HTTP exceptions
- BadRequestException: raised when the request is unprocessable.
- BadRequestException: raised when validation error occurs.
- AuthenticationException: raised when the request is not authenticated.
- RecordNotFoundException: raised when the record doesn't exist in a database.
- DuplicateRecordException: raised when the record already exists in a database.
- InvalidRequestException: raised when a validation error occurs.
"""
from http import HTTPStatus
from typing import Optional

from requests.exceptions import RequestException


class AbstractException(BaseException):
    """The base class for all non-exit exceptions. """
    
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class NotImplementedException(AbstractException):
    pass


class HttpException(RequestException):
    """Base class for all custom HTTP exceptions."""
    
    def __init__(self, status_code: int, message: Optional[str] = None) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(status_code, message)


class BadRequestException(HttpException):
    """A BadRequestException is raised when the request is unprocessable."""
    
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(status_code=HTTPStatus.BAD_REQUEST.value, message=message)


class AuthenticationException(HttpException):
    """An AuthenticationException exception is raised for unauthenticated user."""
    
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(status_code=HTTPStatus.UNAUTHORIZED.value, message=message)


class RecordNotFoundException(HttpException):
    """A RecordNotFoundException is raised when a record is not found in a database."""
    
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(status_code=HTTPStatus.NOT_FOUND.value, message=message)


class DuplicateRecordException(HttpException):
    """A DuplicateRecordException is raised when a duplicate record exists in a database."""
    
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(status_code=HTTPStatus.CONFLICT.value, message=message)


class InvalidRequestException(HttpException):
    """An InvalidRequestException is raised when a validation error occurs."""
    
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(status_code=HTTPStatus.UNPROCESSABLE_ENTITY.value, message=message)
