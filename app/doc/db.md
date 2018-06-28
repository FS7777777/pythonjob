需要安装第三方库
pip install flask-marshmallow
pip install flask-sqlalchemy marshmallow-sqlalchemy
pip install marshmallow-sqlalchemy

https://blog.igevin.info/posts/flask-rest-serialize-deserialize/
https://www.jianshu.com/p/594865f0681b


序列化
from marshmallow import pprint

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result.data)

json_result = schema.dumps(user)
pprint(json_result.data)

反序列化
这样每次调用load()方法时，会按照make_user的逻辑，返回一个User类对象。
user_data = {
    'name': 'Ronnie',
    'email': 'ronnie@stones.com'
}
schema = UserSchema()
result = schema.load(user_data)
result.data  # => <User(name='Ronnie')>

通过接口接收json参数
data = json.loads(request.get_data())
print(data)
user_schema = UserSchema()
data, errors = user_schema.load(data)


#嵌套json序列化
import datetime as dt
from marshmallow import Schema, fields, pprint

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()
        self.friends = []
        self.employer = None

class Blog(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author  # A User object

class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()

class BlogSchema(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema)


user = User(name="Monty", email="monty@python.org")
blog = Blog(title="Something Completely Different", author=user)
result, errors = BlogSchema().dump(blog)
pprint(result)