from asyncio import events
from django.shortcuts import render, get_object_or_404
from events.models import Event
from datetime import date, datetime

# Create your views here.
def details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {'event':event})


def list(request):
    today = datetime.today()
    filter_map = {
        'title': 'title__icontains',
        'is_free': 'cost__exact',
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    events = Event.objects.filter(datetime__gte=today).filter(**filters).order_by('datetime')
    return render(request, 'events/list.html', {'events': events})
    
    
    
    
    
    # query_params = request.GET    
    # if 'title' in query_params and query_params['title'] != "":
    #     events = Event.objects.filter(title__icontains=query_params['title'])
    # else:
    #     events = Event.objects.all()
    # return render(request, 'events/list.html',{'events': events})

    # events = Event.objects.all().order_by('datetime')
    # return render(request, 'events/list.html',{'events':events})
    
   
