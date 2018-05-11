from flask import (Blueprint,request)

api = Blueprint('blog', __name__)

@api.route('/', methods=('GET', 'POST'))
def index():
    print('index')
    return "index"
