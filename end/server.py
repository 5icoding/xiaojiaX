from flask import Flask
from flask_restx  import Api, Resource, fields
from flask_cors import CORS

from .todo import TodoDAO

#def create_app():
    
app = Flask(__name__)
CORS(app)
# 直接将核心对象app作为参数
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')


if __name__ == '__main__':
    app.run(debug=True)