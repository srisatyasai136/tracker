from django.urls import path
from .views import save_location

urlpatterns=[
 path('location/',save_location)
]