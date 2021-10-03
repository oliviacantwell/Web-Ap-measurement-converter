from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def convert(request):
    return render(request, 'convert.html',{'name': 'Olivia'})


def add(request):
    print(request.GET, request.method)
    value1 = request.GET['type1']
    value2 = request.GET['type2']

    num1 = request.GET['num1']

    if (value1 == 'me'):
        
        if (value2 == 'ya'):
            res = float(num1) * 1.09
        
        elif (value2 == 'fe'):
            res = float(num1) * 3.28
        
        elif (value2 == 'in'):
            res = float(num1) * 39.37
        
    elif (value1 == 'ce'):
        
        if (value2 == 'ya'):
            res = float(num1) / 91.44
        
        elif (value2 == 'fe'):
            res = float(num1) / 30.48
        
        elif (value2 == 'in'):
            res = float(num1) / 2.54
        
    elif (value1 == 'mi'):

        if (value2 == 'ya'):
            res = float(num1) / 914
        
        elif (value2 == 'fe'):
            res = float(num1) / 305
        
        elif (value2 == 'in'):
            res = float(num1) / 25.4
    

    else:
        res = 0
    
    return render(request, 'result.html', {'result':res})

