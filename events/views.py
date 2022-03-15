
from django.shortcuts import render, get_object_or_404, redirect
from events.models import Event
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

def get_user_profile(request):
    if request.user.is_authenticated:
        [profile, created] = UserProfile.objects.get_or_create(user=request.user)
        return profile

# Create your views here.
@login_required
def add_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.add(event)
    return redirect("events_list")


@login_required
def remove_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(event)
    return redirect("events_list")

def dashboard(request):
    today = datetime.today()
    user_profile = get_user_profile(request)
    futureattend = user_profile.attending.filter(datetime__gte=today)
    pastattend = user_profile.attending.filter(datetime__lte=today)
    return render(request, 'events/dashboard.html', {'future':futureattend,'past':pastattend})

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

    events = Event.objects.filter(**filters).order_by('datetime')
    return render(request, 'events/list.html', {'events': events})
    
    
    
    
    
    # query_params = request.GET    
    # if 'title' in query_params and query_params['title'] != "":
    #     events = Event.objects.filter(title__icontains=query_params['title'])
    # else:
    #     events = Event.objects.all()
    # return render(request, 'events/list.html',{'events': events})

    # events = Event.objects.all().order_by('datetime')
    # return render(request, 'events/list.html',{'events':events})
    
   
