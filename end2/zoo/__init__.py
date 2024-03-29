from flask_restx import Api

from .cat import api as cat_api
from .dog import api as dog_api
from .course import api as course_api
from .case import api as case_api

api = Api(
    title="Zoo API",
    version="1.0",
    description="A simple demo API",
)

api.add_namespace(cat_api)
api.add_namespace(dog_api)
api.add_namespace(course_api)

api.add_namespace(case_api)
