from django.urls import path
from .views import create_user_view,profile_view

urlpatterns = [
    path('',),
    path('',profile_view)
]
