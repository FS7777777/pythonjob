from flask import (jsonify, request)
import json
from .api_route import api
from ..module import db, Department, DepartmentSchema


@api.route('/depts', methods=['GET'])
def get_depts():
    '''获取所有部门'''
    depts = Department.query.all()
    result, errors = DepartmentSchema().dump(depts, many=True)
    if(len(errors)>0):
        return jsonify({'code':0,'msg':'获取失败','data':[]})
    return jsonify({'code':1,'msg':'添加成功','data':result})

@api.route('/dept', methods=['POST'])
def dept_add():
    '''新增部门'''
    data = json.loads(request.get_data())
    print(data)

    department_schema = DepartmentSchema()
    print(department_schema.load(data).errors)
    db.session.add(department_schema.load(data).data)
    db.session.commit()
    return jsonify({'code':1,'msg':'添加成功','data':data})

@api.route('/dept', methods=['PUT'])
def modify():
    '''修改部门'''
    data = json.loads(request.get_data())
    print(data)
    Department.query.filter_by(id=data['id']).update(data)
    db.session.commit()
    return jsonify({'code':1,'msg':'修改成功','data':data})

@api.route('/dept/<int:dept_id>', methods=['GET','DELETE'])
def delete(dept_id):
    '''删除部门'''
    print('dept_id %d' % dept_id)
    result = Department.query.filter_by(id=dept_id).first()
    print(result)
    db.session.delete(result)
    db.session.commit()
    result = DepartmentSchema().dump(result).data
    return jsonify({'code':1,'msg':'删除成功','data':result})
