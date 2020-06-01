#
# Main APP views
#

from datetime import datetime
from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):
    template_name = 'index.html'

    def get(self):
        timestamp = datetime.now().timestamp()
        return render_template(self.template_name, timestamp=timestamp)
