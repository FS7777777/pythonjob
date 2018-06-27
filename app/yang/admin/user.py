from flask import (jsonify, request)
import json
from .api_route import api
from ..module import db, User, UserSchema


@api.route('/user', methods=['POST'])
def user_add():
    data = json.loads(request.get_data())
    print(data)
    user_schema = UserSchema()
    print(user_schema.load(data).errors)
    # print(user_schema.load(data).data)
    # db.session.add(user_schema.load(data).data)
    # db.session.commit()
    return 'data'