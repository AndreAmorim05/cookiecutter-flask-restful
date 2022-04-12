from .blueprints import api, errors, website
from .routes.api import init_api_routes
from .routes.website import init_site_routes
from .views.error_handler import init_error_routes


def init_app(app):
    init_site_routes(website)
    init_error_routes(errors)
    init_api_routes(api)

    app.register_blueprint(website)
    app.register_blueprint(errors)
    app.register_blueprint(api)
