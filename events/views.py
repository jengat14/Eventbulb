from django.shortcuts import render
from events.models import Event

# Create your views here.
def details(request):
    return render(request, 'events/details.html')

def list(request):
    events = Event.objects.all().order_by('datetime')
    return render(request, 'events/list.html',{'events':events})

