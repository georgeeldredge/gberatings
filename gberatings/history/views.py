from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from history.models import Teamindex
#from history.models import Seasonindex
from history.models import Seasondata

def index(request):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	# QUERY THE DB FOR A LIST OF TEAMS PRESENT
	team_list = Teamindex.objects.order_by('teamname')
	context_dict = {'teams': team_list}

	# RENDER THE RESPONSE AND FIRE IT BACK
	return render_to_response('index.html', context_dict, context)

def history_report(request, team_name):
	# Obtain the context from the HTTP request.
	context = RequestContext(request)

	team_check = Teamindex.objects.filter(teamname=team_name)

	if not team_check: # REPORT THAT THE TEAM DOES NOT SEEM TO EXIST
		message = "Team is nonexistant"
		team_info = ''
		team_data = ''
	else: # GO GET THIS TEAM'S DATA
		message = ''

		team_info = Teamindex.objects.get(teamname=team_name)
		team_id = team_info.id
			
		# GO GET ALL COMPLETED SEASON DATA FROM THE DB FOR THIS TEAM
		team_data = Seasondata.objects.filter(teamid=team_id)
#		team_data = Seasondata.objects.filter(teamid=team_id).extra(select={'weekfinalrating*1000 as weekfinalratingadjusted'})

	context_dict = {'teamname': team_name, 'teaminfo': team_info, 'message': message, 'teamdata': team_data}

	# RENDER THE RESPONSE AND FIRE IT BACK
	return render_to_response('history.html', context_dict, context)
