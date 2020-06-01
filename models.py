#
# Base APP models
#

from flask import Flask, Blueprint
from config import CURRENT_CONFIG


application = Flask(
    __name__,
    template_folder='frontend/public',
    static_folder='frontend/static'
)
application.config.from_object(CURRENT_CONFIG)
blueprint = Blueprint(
    'static2',
    __name__,
    static_url_path='/static/favicon',
    static_folder='frontend/public'
)
application.register_blueprint(blueprint)
