#
# Main APP URLs
#

from backend.models import application
from backend import views
from backend import api_views


API_VERSION = 'v1'

# Views
application.add_url_rule(
    '/',
    view_func=views.IndexView.as_view('index_view')
)

# APIs
application.add_url_rule(
    f'/api/{API_VERSION}/first-example/',
    view_func=api_views.APIFirstExample.as_view('first_example_api')
)
application.add_url_rule(
    f'/api/{API_VERSION}/second-example/',
    view_func=api_views.APISecondExample.as_view('second_example_api')
)
