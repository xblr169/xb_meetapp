#!/usr/bin/python
# -*-encoding=utf8 -*-

class ReturnCode:
    SUCCESS = 0
    FAILED = -100
    WRONG_PARMAS = -101
    RESOURCE_NOT_FOUND = -102
    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501

    @classmethod
    def messgae(cls,code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.WRONG_PARMAS:
            return 'wrong params'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.RESOURCE_NOT_FOUND:
            return 'resource not found'


def wrap_json_response(data=None,code=None,message=None):
    response ={}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.messgae(code)
    if data is not None:
        response['data'] = data

    response['result_code'] = code
    response['message'] = message
    return response

class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(cls,data=None, code=None, message=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            message = ReturnCode.messgae(code)
        if data is not None:
            response['data'] = data
        response['result_code'] = code
        response['message'] = message
        return response
