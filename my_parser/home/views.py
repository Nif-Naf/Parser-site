from turtle import title
from django.shortcuts import render
from django.views.generic import View
import requests
from .forms import Parsing_form
from bs4 import BeautifulSoup as BS

def show(request):  #home_form
    """Просмотр главной страниц."""

    output = {
        'form': Parsing_form
    }

    return render(request, 'home/home.html', output)

def show_result(request):   #table
    """Просмотр страницы с результатом."""
    return render(request, 'home/result.html')

class Parse(View):
    """ """

    def get(self, request):
        """ """

        input_form = Parsing_form(request.GET)

        if input_form.is_valid:
            """ """
            a = []
            get_adress = request.GET['url']
            
            addr = requests.get('https://stopgame.ru/review/new/izumitelno/p2')
            html = BS(addr.content, 'html.parser')

            for el in html.select(".items > .article-summary"):
                title = el.select('.caption > a')
                res = title[0].text
                a.append(res)

            output = {
            'RES': a
        }

        return render(request, 'home/result.html', output)