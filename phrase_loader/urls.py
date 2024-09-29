from django.urls import path
from phrase_loader import views

app_name = "phrase_loader"

urlpatterns = [
    path('phrase_loader/',view=views.index,name='index')
]
