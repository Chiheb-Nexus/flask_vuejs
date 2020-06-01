#
# Main APP URLs
#

from models import application
import views


application.add_url_rule(
    '/', view_func=views.IndexView.as_view('index_view')
)
