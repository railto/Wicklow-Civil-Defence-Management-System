from flask_restx import Api

from app.routes.auth import ns as auth_ns
from app.routes.users import ns as users_ns

api = Api(version='1.0.0', title='Wicklow Civil Defence Management API', doc='/docs')

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(users_ns, path='/users')