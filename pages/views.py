from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('<h1>This is an http response for index</h1>')
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
def test(request):
    return HttpResponse('''
                            <h1>This is an http response for test</h1>
                            <h1>This is 2nd line</h1>
                        ''')
    
def template(request):
    return render(request, 'home/index.html')