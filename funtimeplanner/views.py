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

    output_list = usermatches(user_list)

    context_dict = {'pairs': output_list,
                    }

    return render_to_response('funtimeplanner/matches.html', context_dict, context)

def usermatches(user_list):
    output_list=[]
    #3. For Every User, Display his matching interests
    for user in user_list:
        output_pair = {}
        output_pair["matches"] = interestMatch(user)
        output_pair["user"] = user
        output_list.append(output_pair)
    return output_list


def interestMatch(user):
    output = {}
    #2. For Every users interest, display his matching events
    for user_interest in user.funinterest_set.all():
        eventMatch(user_interest, output)
    return output

def eventMatch(user_interest, output):
    event_list = FunEvent.objects.all()
    #1. For Every event, if the users interest is in Events Description or Events Name, build a dictionary for such events
    for event in event_list:
        if user_interest.name in event.Description or user_interest.name in event.name:
            output[event.id] = event

def userlist_display(request):
    user_list = User.objects.all()
    context = RequestContext(request)
    context_dict = {'users' : user_list
    }
    return render_to_response('funtimeplanner/userlist.html', context_dict, context)























