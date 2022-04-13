from django.urls import path
from . import views
from .views import Parse

urlpatterns = [
    path('', views.show, name="home_form"),
    path('result', views.show_result, name="table"),

    # path('send', views.send_result, name="result"),
    path('send', Parse.as_view(), name='result'),
]
