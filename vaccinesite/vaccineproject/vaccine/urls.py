from django.urls import path
from . import views
app_name = 'vaccine'

urlpatterns = [
    path('', views.vaccinePerson, name='vaccinePerson'),
    path('details/', views.details, name='details'),
    path('details/register', views.details, name='details'),
]
