from flask_restx import Namespace, Resource, fields

api = Namespace("cases", description="cases related operations")

case = api.model(
    "Case",
    {
        "title": fields.String(required=True, description="The course title")
    },
)

@api.route('/case')
# 定义子路由,如果没有的话，传空字符串即可
class Case(Resource):
    # 定义restful 风格的方法
    def get(self):
        return {'code': 0, 'msg': 'get success'}

    def post(self):

        return {'code': 0, 'msg': 'post success'}

    def put(self):
        return {'code': 0, 'msg': 'put success'}

    def delete(self):
        return {'code': 0, 'msg': 'delete success'}