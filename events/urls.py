from . import views
from django.urls import path

urlpatterns = [
    path('details',views.details,name="details")
]
