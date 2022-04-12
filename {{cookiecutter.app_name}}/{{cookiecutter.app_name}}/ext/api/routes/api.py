from flask_restful import Api
from {{cookiecutter.app_name}}.ext.api.views.api import ApiArea


def init_api_routes(api):
    ApiRest = Api(api)
    ApiRest.add_resource(ApiArea, "/post", endpoint="api-post")
