from msilib.schema import ListView
from django.urls import path
from . import views
from .views import Parse, Show_tablet


urlpatterns = [
    path('', views.show, name="home_form"),
   
    path('test', views.test, name="test"),
    path('test_two', views.test_two, name="test_two"),

    # path('send', views.send_result, name="result"),
    path('send', Parse.as_view(), name='result'),

    # path('result', views.show_result, name="table"),
    path('result', Show_tablet.as_view(), name="table"),
]
