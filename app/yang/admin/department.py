from flask import (jsonify, request)
from .api_route import api
from ..module import db, Department


@api.route('/depts', methods=['GET'])
def get_depts():
    '''获取所有部门'''
    pass

@api.route('/dept', methods=['POST'])
def add(args):
    '''新增部门'''
    data = json.loads(request.get_data())

    dept = Department()
    print(data)
    return data

@api.route('/dept', methods=['PUT'])
def modify():
    '''修改部门'''
    data = json.loads(request.get_data())
    print(data)
    return data

@api.route('/dept/<int:dept_id>', methods=['GET','DELETE'])
def delete(dept_id):
    '''删除部门'''
    print('dept_id %d' % dept_id)
    return 'dept_id %d' % dept_id