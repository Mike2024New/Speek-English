from django.shortcuts import render



def index(request):
    context={
        'title':'phrase_loader',
    }
    return render(request, 'phrase_loader/index.html',context)
