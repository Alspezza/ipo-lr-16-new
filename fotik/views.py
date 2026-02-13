from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('''
<a>Главная страница</a>
<li>
            <a href="http://127.0.0.1:8000/fotera/">О сайте</a>
</li>
<li>
            <a href="http://127.0.0.1:8000/author/">Об авторе</a>
</li>
''')

def author(request):
    return HttpResponse('''
<p><strong>Имя:</strong> Специан Захар Александрович</p>
        <p>програмист да все дела 16yo красава</p>
        <p style="color: #888;">// Это всё</p>''')

def fotera(request):
    return HttpResponse('''
<a>Fotera - интернет магазин фотоаппаратов и другой фототехники(возможно скам)<a/>
<a href="https://fotera.by/">Ссылка на оригинальный сайт</a>''')
