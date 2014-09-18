from django.shortcuts import render
from funtimeplanner.models import FunInterest, FunEvent
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    context = RequestContext(request)
    interest_list = FunInterest.objects.all()
    context_dict = {'interests': interest_list}

    return render_to_response('funtimeplanner/index.html', context_dict, context)


