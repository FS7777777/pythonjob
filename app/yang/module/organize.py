
from .. import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    superior_id = db.Column(db.Integer)
    fullname = db.Column(db.String(64))
    organization_code = db.Column(db.String(32))
    organization_type = db.Column(db.String(32))
    sort_number = db.Column(db.Integer)

    def __repr__(self):
        return '<Department \'%s\'>' % self.fullname
        