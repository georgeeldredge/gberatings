from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from history.models import Teamindex


def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of teams in the ratings db.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    team_list = Teamindex.objects.order_by('teamname')
    context_dict = {'teams': team_list}

    # Render the response and send it back!
    return render_to_response('index.html', context_dict, context)
