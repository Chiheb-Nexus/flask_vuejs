#
# WSGI entry point
#

from backend.models import application

PORT = 8080
HOST = '127.0.0.1'


if __name__ == '__main__':
    from backend.urls import *  # noqa: F401,F403
    application.run(port=PORT, host=HOST)
