from django.shortcuts import render, get_object_or_404
from events.models import Event

# Create your views here.
def details(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {'event':event})


def list(request):
    events = Event.objects.all().order_by('datetime')
    return render(request, 'events/list.html',{'events':events})

