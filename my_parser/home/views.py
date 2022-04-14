from turtle import title
from django.shortcuts import render
from django.views.generic import View
import requests
from .forms import Parsing_form
from bs4 import BeautifulSoup as BS

from .models import Result

def show(request):  #home_form
    """Просмотр главной страниц."""

    output = {
        'form': Parsing_form
    }

    return render(request, 'home/home.html', output)

def show_result(request):   #table
    """Просмотр страницы с результатом."""
    return render(request, 'home/result.html')

def test(request):   #test
    """Просмотр страницы с результатом."""
    return render(request, 'home/test.html')

class Parse(View):
    """ """

    def get(self, request):
        """ """

        input_form = Parsing_form(request.GET)

        if input_form.is_valid:
            """ """
            a = []
            b = []

            # Получаем адрес страницы из запроса.
            get_adress = request.GET['url']
            
            #Переходим на запрошенную страницу.
            addr = requests.get(get_adress)

            #Создаем экземпляр класса
            html = BS(addr.content, 'html.parser')

            # https://api.domainsdb.info/v1/domains/search?domain=
            # https://api.domainsdb.info/v1/domains/search?domain=http://127.0.0.1:8000/test
            # https://api.domainsdb.info/v1/domains/search?domain=https://nif-resume.xyz/

            # Находим все теги а на странице
            for link in html.find_all('a'):
                a.append(link.get('href'))

            # Выбираем какие на нужны поля
            para = dict(
                dom = 'domains',
                dat = 'create_date'
            )

            
            
            # Получаем информацию о ссылке через апи.
            for i in a:
                adress_api = ('https://api.domainsdb.info/v1/domains/search?domain=' + i)
                addr_api = requests.get(adress_api, para)
                # b.append(addr_api.json())
                

            # Result 
            result = addr_api.json()

            # Как созранить их в БД?
            for i in result:

                sdb = Result(
                    url = '', 
                    domains = 'domain',
                    create_data = 'create_date',
                    update_data = 'update_date',
                    country = 'country',
                    is_dead = 'is_Dead',
                    a = 'A',
                    ns = 'NS',
                    cname = 'CNAME',
                    mx = 'MX',
                    txt = 'TXT'
                )

                sdb.save()

            output = {
            # 'RES': addr_api
            'Score': len(a),
            'Href': a,
            'API': addr_api.json()
        }

        return render(request, 'home/result.html', output)