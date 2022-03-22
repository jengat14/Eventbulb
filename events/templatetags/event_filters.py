# events/templatetags/event_filters.py
from django import template
from datetime import datetime
from accounts.models import UserProfile
from events.models import Event 

register = template.Library()


@register.filter
def is_attending(user, event):
        return user.profile.attending.filter(id=event.id).exists()

@register.filter
def has_attended(user, event):
        today = datetime.today()
        return user.profile.attending.filter(id=event.id).filter(datetime__lt=today).exists()

