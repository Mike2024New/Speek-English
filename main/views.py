from django.shortcuts import render

def index(request):
    context={
        'title':'speack English'
    }
    return render(request, 'main/index.html',context)
