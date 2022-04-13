from django.shortcuts import render

def show_table(request):
    return render(request, 'table/table.html')