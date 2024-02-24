from flask_restx import Namespace, Resource, fields

from end2.extensions import db

api = Namespace("courses", description="Course related operations")


course = api.model(
    "Course",
    {
        "id": fields.String(required=True, description="The course identifier"),
        "parentId": fields.String(required=True, description="The course parentId"),
        "title": fields.String(required=True, description="The course title"),
        "description": fields.String(required=True, description="The course description"),
        "filePath": fields.String(required=True, description="The course filePath"),
        "createTime": fields.String(required=True, description="The course createTime")
    },
)



class TmpCourse(db.Model):
    __tablename__ = 'tmp_courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parentId = db.Column(db.Integer)
    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    filePath = db.Column(db.String(50))
    createTime = db.Column(db.DateTime)

parser = api.parser()
parser.add_argument(
    "course", type=str, required=True, help="The task details", location="form"
)

@api.route("/")
class CoursesList(Resource):
    @api.doc("list_courses")
    @api.marshal_list_with(course)
    def get(self):
        """List all dogs"""
        #return Courses
        courses = TmpCourse.query.all()
        for user in courses:
            print(user.id, user.title)
        return courses
    
    @api.doc(parser=parser)
    @api.marshal_with(todo)
    def put(self, todo_id):
        """Update a given resource"""
        args = parser.parse_args()
        task = {"task": args["task"]}
        TODOS[todo_id] = task
        return task

    
