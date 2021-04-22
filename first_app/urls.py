from django.urls import path,include
from . import views

app_name='first_app'

urlpatterns = [
    path('',views.profile_homepage,name='profile_homepage')
]
