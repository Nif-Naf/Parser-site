from re import template
from turtle import title
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from .forms import Parsing_form, Js_form, Search_form
from bs4 import BeautifulSoup as BS
import json
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from .models import Result, Search
import datetime

def show(request):  
    """Просмотр главной страниц."""

    output = {
        'form': Parsing_form,
    }

    return render(request, 'home/home.html', output)

class Show_tablet(ListView):
    """Класс отвечающий за вывод и форматирование таблицы."""
    model = Result
    template_name = 'home/result.html'
    context_object_name = 'result'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        """Добавляем форму поиска для страницы."""
        context = super().get_context_data(**kwargs)
        context['search'] = Search_form()
        return context

class Show_sorting_table_for_request(Show_tablet):
    """"Класс для вывода обьектов по поисковому запросу."""

    def get_queryset(self):
        """Данная функция 'отбирает' нужные обьекты в соответствии с поисковым запросом."""

        if self.request.GET.get("search_object"):
            """ """
            selection = self.request.GET.get("search_object")
            query = Result.objects.filter(url__icontains = selection)
            return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_obj'] = self.request.GET.get("search_object")
        return context

class Sorting_by_url(Show_tablet):
    """Сортируем по адресу."""

    def get_ordering(self):
        return self.request.GET.get('ordering', '-url')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'url'
        return context

class Sorting_by_dead(Show_tablet):
    """Сортируем по состоянию."""

    def get_ordering(self):
        return self.request.GET.get('ordering', '-is_dead')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'dead'
        return context

class Sorting_by_country(Show_tablet):
    """Сортируем обькты по странам."""

    def get_ordering(self):
        return self.request.GET.get('ordering', '-country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'country'
        return context
    
class Sorting_by_create_data(Show_tablet):
    """Сортируем обьекты по дате создания."""

    def get_ordering(self):
        return self.request.GET.get('ordering', '-create_data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'create_data'
        return context

class Sorting_by_update_data(Show_tablet):
    """Сортируем обьекты по дате обновления."""

    def get_ordering(self):
        return self.request.GET.get('ordering', '-update_data')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'update_data'
        return context

class Parse(View):
    """Парсер."""

    def get(self, request):
        """Если приходит в класс запрос Get"""

        input_form = Parsing_form(request.GET)

        if input_form.is_valid:
            """Если форма валидна."""
         
            # Получаем адрес страницы из запроса.
            get_adress = request.GET['url']
            
            #Переходим на запрошенную страницу.
            addr = requests.get(get_adress)

            #Создаем экземпляр класса
            html = BS(addr.content, 'html.parser')

            # Находим все теги а на странице
            for link in html.find_all('a'):
                
                #Получаем ссылку в теге а
                teg = link.get('href')
                
                #Формируем адресс для передачи в АПИ
                adress_api = ('https://api.domainsdb.info/v1/domains/search?domain=' + teg)

                #Отправка ссылки в АПИ
                addr_api = requests.get(adress_api) #<Response [200]> 

                #Получаем информацию о ссылке через апи. В формате джейсон
                result = addr_api.json() #Jsone файл

                funct = self.savedatabasejsone(result, teg)
                
        return redirect('table')

    def savedatabasejsone(self, result, teg): 
        """ Преобразовываем и добавляем в БД."""

        res = result['domains']
        
        for i in res:
            convertait = self.convert_date(i)
            i['create_date'] =  convertait[0]
            i['update_date'] =  convertait[1]

            newRecord = Result(
                url = teg, 
                domains = i['domain'],
                create_data = i['create_date'],
                update_data = i['update_date'],
                country = i['country'],
                is_dead = i['isDead'],
                a = i['A'],
                ns = i['NS'],
                cname = i['CNAME'],
                mx = i['MX'],
                txt = i['TXT']
                )
            newRecord.save()
        
        return "Все обьекты добавлены в базу данных успешно."

    def convert_date(self, i):
        """Конвертируем дату."""

        b = i['create_date']
        q = b.split('.')
        w = datetime.datetime.strptime(q[0], "%Y-%m-%dT%H:%M:%S")

        y = i['update_date']
        l = y.split('.')
        z = datetime.datetime.strptime(l[0], "%Y-%m-%dT%H:%M:%S")

        return (w, z)

def test(request):   #test
    """Просмотр страницы с результатом."""
    return render(request, 'home/test.html')

def test_two(request):   #test
    """Просмотр страницы с результатом."""
    return render(request, 'home/test_two.html')