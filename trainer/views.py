from django.shortcuts import redirect, render
from random import randint

test_phrase = [{'ru': 'Мой брат хочет попытаться сделать это.', 'en': 'My brother wants to try to do it.'},
     {'ru': 'Я хочу знать английский.', 'en': 'I want to know English.'},
     {'ru': 'Это часто случается.', 'en': 'It often happens.'},
     {'ru': 'Моя тетя хочет продать свой дом.', 'en': 'My aunt wants to sell her house.'},
     {'ru': 'Я хочу играть в эту компьютерную игру.', 'en': 'I want to play this computer game.'},
     {'ru': 'Я хочу лететь в Нью -Йорк.', 'en': 'I want to fly to New York.'},
     {'ru': 'Он хочет знать все.', 'en': 'He wants to know everything.'},
     {'ru': 'Я хочу позвонить ему.', 'en': 'I want to call him.'},
     {'ru': 'Моя сестра хочет купить это платье.', 'en': 'My sister wants to buy this dress.'},
     {'ru': 'Я хочу прочитать эту книгу.', 'en': 'I want to read this book.'},
     {'ru': 'Я голоден.', 'en': 'I want to eat.'},
     {'ru': 'Я хочу кофе.', 'en': 'I want coffee.'},
     {'ru': 'Мой родственник хочет играть в эту игру.', 'en': 'My relative wants to play this game.'},
     {'ru': 'Его секретарь хочет найти новую работу.', 'en': 'His secretary wants to find a new job.'},
     {'ru': 'Я хочу иметь свой собственный бизнес.', 'en': 'I want to have my own business.'},
     {'ru': 'Я хочу вам помочь.', 'en': 'I want to help you.'},
     {'ru': 'Я хочу поехать в Америку в следующем месяце.', 'en': 'I want to go to America next month.'},
     {'ru': 'Я хочу пойти в кино.', 'en': 'I want to go to the cinema.'},
     {'ru': 'Мой босс хочет все знать.', 'en': 'My boss wants to know everything.'},
     {'ru': 'Я хочу купить дом.', 'en': 'I want to buy a house.'}]

def result(request):
    print(request.session['current_answer'])
    if request.session['current_answer']==request.session['current_phrase']['en']:
        result={
            "status":True,"en":request.session['current_phrase']["en"],"ru":request.session['current_phrase']["ru"],
            'answer':request.session['current_answer']
            }
    else:
        result={"status":False,"en":request.session['current_phrase']["en"],"ru":request.session['current_phrase']["ru"],
                'answer':request.session['current_answer']
                }
    context = {
        'title':'Результат',
        'result':result,
    }
    return render(request,'trainer/result.html',context)

def index(request):
    if 'current_phrase' not in request.session:
        request.session['current_phrase'] = {'ru':None, 'en':None}
    if 'current_answer' not in request.session:
        request.session['current_answer'] = None

    if request.method == 'POST':
        request.session['current_answer'] = request.POST['answer']
        return redirect('trainer:result')


    phrase = test_phrase[randint(0,len(test_phrase)-1)]
    request.session['current_phrase']['ru']= phrase['ru']
    request.session['current_phrase']['en']= phrase['en']
    request.session.modified = True

    context = {
        'title':'trainer',
        'phrase':request.session['current_phrase']['ru']
    }
    return render(request, 'trainer/index.html',context)
