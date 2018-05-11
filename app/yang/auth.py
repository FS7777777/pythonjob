from flask import (Blueprint,request)

api = Blueprint('auth', __name__, url_prefix='/auth')

@api.before_request
def check_load():
    print('just check_load')

@api.route('/login', methods=('GET', 'POST'))
def login():
    print('sign in')
    return "sign in"


@api.route('/logout')
def logout():
    print('sign in')
    return "sign out"