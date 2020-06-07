#
# Base APP models
#

import os
import pathlib
from flask import Flask, Blueprint
from backend.config import CURRENT_CONFIG


BASE_DIR = str(pathlib.Path(__file__).parent.absolute().parent)

application = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'frontend', 'public'),
    static_folder=os.path.join(BASE_DIR, 'frontend', 'static')
)
application.config.from_object(CURRENT_CONFIG)
blueprint = Blueprint(
    'static2',
    __name__,
    static_url_path=os.path.join(BASE_DIR, 'frontend', 'static', 'favicon'),
    static_folder=os.path.join(BASE_DIR, 'frontend', 'public')
)
application.register_blueprint(blueprint)
