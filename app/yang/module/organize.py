
from .. import db, ma

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    phone = db.Column(db.String(11))
    password = db.Column(db.String(32), nullable=False,default='000000')
    dept_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)
    is_enable = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<User %r>' % self.fullname



class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    #上级部门id
    superior_id = db.Column(db.Integer, nullable=False)
    fullname = db.Column(db.String(64), nullable=False)
    #机构代码
    organization_code = db.Column(db.String(32), nullable=False)
    #机构类型
    organization_type = db.Column(db.String(32), nullable=False)
    #排序号
    sort_number = db.Column(db.Integer)
    #排序号
    level = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return '<Department \'%s\'>' % self.fullname


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class DepartmentSchema(ma.ModelSchema):
    class Meta:
        model = Department
        