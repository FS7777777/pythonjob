from flask import (jsonify, request, abort, make_response)
import json
from .api_route import api
from ..module import db, User, UserSchema


@api.route('/users/<int:dept_id>', methods=['GET'])
def get_users(dept_id):
    '''获取部门下所有人员'''
    users = User.query.filter_by(dept_id=dept_id).all()
    result, errors = UserSchema().dump(users, many=True)
    if(len(errors)>0):
        return jsonify({'code':0,'msg':'获取失败','data':[]})
    return jsonify({'code':1,'msg':'获取成功','data':result})

@api.route('/user', methods=['POST'])
def user_add():
    data = json.loads(request.get_data())
    print(data)
    user_schema = UserSchema()
    print(user_schema.load(data).errors)
    db.session.add(user_schema.load(data).data)
    db.session.commit()
    return jsonify({'code':1,'msg':'添加成功','data':data})

@api.route('/user', methods=['PUT'])
def user_modify():
    '''修改人员'''
    data = json.loads(request.get_data())
    print(data)
    User.query.filter_by(id=data['id']).update(data)
    db.session.commit()
    return jsonify({'code':1,'msg':'修改成功','data':data})

@api.route('/user/<int:user_id>', methods=['GET','DELETE'])
def user_delete(user_id):
    '''删除人员'''
    print('user_id %d' % user_id)
    result = User.query.filter_by(id=user_id).first()
    print(result)
    db.session.delete(result)
    db.session.commit()
    result = UserSchema().dump(result).data
    return jsonify({'code':1,'msg':'删除成功','data':result})


@api.route('/resetpwd/<int:user_id>', methods=['GET'])
def user_reset(user_id):
    '''重置密码'''
    print('user_id %d' % user_id)
    result = User.query.filter_by(id=user_id).update({'password':'111111'})
    print(result)
    db.session.commit()
    return jsonify({'code':1,'msg':'成功','data':None})