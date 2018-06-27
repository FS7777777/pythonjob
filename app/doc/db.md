需要安装第三方库
pip install flask-marshmallow
pip install flask-sqlalchemy marshmallow-sqlalchemy
pip install marshmallow-sqlalchemy

https://blog.igevin.info/posts/flask-rest-serialize-deserialize/


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