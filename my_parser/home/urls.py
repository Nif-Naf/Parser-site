from django.urls import path
from . import views
from .views import Parse, Show_tablet, Sorting_by_create_data, Sorting_by_update_data, Sorting_by_country, Sorting_by_url, Sorting_by_dead, Show_sorting_table_for_request


urlpatterns = [

    #Рендерим главную страницу.
    path('', views.show, name="home_form"),
   
    #Сам парсер.
    path('send', Parse.as_view(), name='result'),

    #Таблица с результатами.
    path('result', Show_tablet.as_view(), name="table"),
    
    # Сортировка по столбцам.
    path('result/search by create_data', Sorting_by_create_data.as_view(), name='search_create_data'),
    path('result/search by update_data', Sorting_by_update_data.as_view(), name='search_update_data'),
    path('result/search by country', Sorting_by_country.as_view(), name='search_country'),
    path('result/search by url', Sorting_by_url.as_view(), name='search_url'),
    path('result/search by dead', Sorting_by_dead.as_view(), name='search_dead'),

    #Поиск.
    path('result/search by request', Show_sorting_table_for_request.as_view(), name='search')
]
