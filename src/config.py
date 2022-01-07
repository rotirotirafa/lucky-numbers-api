from enum import Enum


class AllowedMethodsEnum(Enum):
    ALL = '*'
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

