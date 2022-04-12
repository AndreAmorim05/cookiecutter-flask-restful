from flask import Blueprint

website = Blueprint("website", __name__)
api = Blueprint("api", __name__, url_prefix="/api")
errors = Blueprint("errors", __name__)
