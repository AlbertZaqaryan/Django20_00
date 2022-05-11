from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):
    mylist = request.POST['mylist']
    number = request.POST['number']

    if number in mylist:
        res = 'Yes'
        return render(request, 'result.html', {'res':res})
    else:
        res = 'No'
        return render(request, 'result.html', {'res':res})