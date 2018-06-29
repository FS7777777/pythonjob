
from .. import db, ma

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(32), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120))
    password = db.Column(db.String(32), nullable=False)
    dept_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username



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
    sort_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Department \'%s\'>' % self.fullname


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class DepartmentSchema(ma.ModelSchema):
    class Meta:
        model = Department
        