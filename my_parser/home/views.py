from django.shortcuts import render, redirect

import requests
from bs4 import BeautifulSoup as BeaSup

from django.views.generic.list import ListView
from django.views.generic import View

from .forms import Parsing_form, Search_form
from .models import Result

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import datetime
import json

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
    paginate_by = 5

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
            """Фильтрация по вхождению по графе url."""
            selection = self.request.GET.get("search_object")
            query = Result.objects.filter(url__icontains = selection)
            return query
    
    def get_context_data(self, **kwargs):
        """Передаем дополнительным параметром поисковый запрос."""
        context = super().get_context_data(**kwargs)
        context['search_obj'] = self.request.GET.get("search_object")
        return context

class Sorting_by_url(Show_tablet):
    """Сортируем по адресу."""

    def get_ordering(self):
        """Правило по которому сортируем выдачу обьектов."""
        return self.request.GET.get('ordering', '-url')

    def get_context_data(self, **kwargs):
        """Передаем участок url, для пагинации."""
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'url'
        return context

class Sorting_by_dead(Show_tablet):
    """Сортируем по состоянию."""

    def get_ordering(self):
        """Правило по которому сортируем выдачу обьектов."""
        return self.request.GET.get('ordering', '-is_dead')
    
    def get_context_data(self, **kwargs):
        """Передаем участок url, для пагинации."""
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'dead'
        return context

class Sorting_by_country(Show_tablet):
    """Сортируем обькты по странам."""

    def get_ordering(self):
        """Правило по которому сортируем выдачу обьектов."""
        return self.request.GET.get('ordering', '-country')

    def get_context_data(self, **kwargs):
        """Передаем участок url, для пагинации."""
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'country'
        return context
    
class Sorting_by_create_data(Show_tablet):
    """Сортируем обьекты по дате создания."""

    def get_ordering(self):
        """Правило по которому сортируем выдачу обьектов."""
        return self.request.GET.get('ordering', '-create_data')

    def get_context_data(self, **kwargs):
        """Передаем участок url, для пагинации."""
        context = super().get_context_data(**kwargs)
        context['part_url'] = 'create_data'
        return context

class Sorting_by_update_data(Show_tablet):
    """Сортируем обьекты по дате обновления."""

    def get_ordering(self):
        """Правило по которому сортируем выдачу обьектов."""
        return self.request.GET.get('ordering', '-update_data')

    def get_context_data(self, **kwargs):
        """Передаем участок url, для пагинации."""
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
            
            valid_get_url = self.validator_url(get_adress)

            if valid_get_url == False:
                """Ссылка не прошла тест."""
                return redirect('home_form')

            elif valid_get_url == True:
                """Ссылка прошла тест."""

                #Переходим на запрошенную страницу.
                adres_html_page = requests.get(get_adress)

                #Создаем экземпляр класса
                html_page = BeaSup(adres_html_page.content, 'html.parser')

                # Находим все теги а на странице
                for link in html_page.find_all('a'):
                    """Цикл для асинхронного добавление информации из API."""
                    
                    #Получаем ссылку в теге а
                    teg_a = link.get('href')
                    
                    #Формируем адресс для передачи в АПИ
                    adres_api = ('https://api.domainsdb.info/v1/domains/search?domain=' + teg_a)

                    #Отправка ссылки в АПИ
                    get_adres_api = requests.get(adres_api) #<Response [200]> 

                    #Получаем информацию о ссылке через апи. В формате джейсон
                    result = get_adres_api.json() #Jsone файл

                    funct = self.savedatabasejsone(result, teg_a)
                    
                    if funct == True:
                        """Если все успешно добавлено без исключений."""
                        continue

                    elif funct == "Exeption":
                        """Если возникли каие-то проблемы останавливаем цикл поиска и записи."""
                        break
        else:
            return redirect('home_form')

        return redirect('table')

    def savedatabasejsone(self, result, teg_a): 
        """Преобразовываем и добавляем в БД."""
        
        try:
            """Здесь обрабатываем возможное исключение."""
            need_dir = result['domains']
            

        except KeyError:
            """Если выброшенно исключени, возвращаемся обратно в цикл. Те просто пропускаем 'проблемную' ссылку."""
            return 'Exeption'
        
        else:
            """Если не было исключения. То продолжаем добавлять информацию из API."""

            for i in need_dir:
                """Цикл записи."""

                convertait = self.convert_date(i)
                i['create_date'] =  convertait[0]
                i['update_date'] =  convertait[1]

                newRecord = Result(
                    url = teg_a, 
                    domain = i['domain'],
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
        
        return True

    def convert_date(self, i):
        """Конвертируем дату."""

        b = i['create_date'].split('.')
        w = datetime.datetime.strptime(b[0], "%Y-%m-%dT%H:%M:%S")

        y = i['update_date'].split('.')
        z = datetime.datetime.strptime(y[0], "%Y-%m-%dT%H:%M:%S")

        return (w, z)

    def validator_url(self, url):
        """Проверяем ссылки на валидность."""

        check_url = URLValidator()

        try:
            """Обработчик."""
            check_url(url)

        except ValidationError:
            """Если ссылка не валидна."""
            return False
        else:
            """В ином случае."""
            return True
