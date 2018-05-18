import json
from flask import (Blueprint,request,make_response)
from flask import jsonify

api = Blueprint('auth', __name__, url_prefix='/auth')

@api.before_request
def check_load():
    print('just check_load')

@api.route('/login', methods=['POST'])
def login():
    data = json.loads(request.get_data())
    print(data)
    # resp.status = 500
    return jsonify(data)


@api.route('/logout')
def logout():
    print('sign in')
    return "sign out"