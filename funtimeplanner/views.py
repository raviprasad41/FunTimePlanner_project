from django.shortcuts import render
from funtimeplanner.models import FunInterest, FunEvent
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    context = RequestContext(request)
    interest_list = FunInterest.objects.all()
    context_dict = {'interests': interest_list}

    return render_to_response('funtimeplanner/index.html', context_dict, context)

def event_matches(request):
    context = RequestContext(request)
    user_list = User.objects.all()
    event_list = FunEvent.objects.all()
    user_interest_list = user_list[1].funinterest_set.all()
    context_dict = {'users': user_list,
                    'events': event_list,
                    'user_interests': user_interest_list,
                    }


    return render_to_response('funtimeplanner/matches.html', context_dict, context)



    #for user_interest in user_interest_list:











