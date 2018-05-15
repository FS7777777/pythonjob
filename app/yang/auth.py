from flask import (Blueprint,request,make_response)

api = Blueprint('auth', __name__, url_prefix='/auth')

@api.before_request
def check_load():
    print('just check_load')

@api.route('/login', methods=('GET', 'POST'))
def login():
    print('sign in')
    # resp = make_response()
    # resp.status = 500
    return 'resp'


@api.route('/logout')
def logout():
    print('sign in')
    return "sign out"