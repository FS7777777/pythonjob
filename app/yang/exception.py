from flask import (Blueprint,request)
"""全局异常处理"""
exception = Blueprint('exception',__name__,url_prefix='/error')

@exception.app_errorhandler(500)
def error(e):
    return 'error'