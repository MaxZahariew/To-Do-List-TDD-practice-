from django.urls import path
from list import views


app_name = 'index'

urlpatterns = [
    path('', views.main, name='main')
]
