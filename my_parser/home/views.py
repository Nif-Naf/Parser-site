from turtle import title
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from .forms import Parsing_form, Js_form
from bs4 import BeautifulSoup as BS
import json

from .models import Result, Messages

def show(request):  #home_form
    """Просмотр главной страниц."""

    output = {
        'form': Parsing_form
    }

    return render(request, 'home/home.html', output)

def show_result(request):   #table
    """Просмотр страницы с результатом."""

    object_in_db = Result.objects.all()
    
    return render(request, 'home/result.html', context = {'result': object_in_db})

class Parse(View):
    """ """

    def get(self, request):
        """ """

        input_form = Parsing_form(request.GET)

        if input_form.is_valid:
            """ """
         
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
              
                funct = self.savedatabasejsone(result, get_adress)

        return redirect('table')

    def savedatabasejsone(self, result, get_adress): 
        """ Преобразовываем и добавляем в БД."""

        res = result['domains']

        for i in res:
            newRecord = Result(
                url = get_adress, 
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

def test(request):   #test
    """Просмотр страницы с результатом."""
    return render(request, 'home/test.html')

def test_two(request):   #test
    """Просмотр страницы с результатом."""
    return render(request, 'home/test_two.html')