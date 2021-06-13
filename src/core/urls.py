from django.urls import path
from .views import create_user_view,profile_view

urlpatterns = [
    path('create-user/',create_user_view),
    path('',profile_view)

]
