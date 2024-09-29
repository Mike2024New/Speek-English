from django.urls import path
from trainer import views

app_name = "trainer"

urlpatterns = [
    path('trainer/',view=views.index, name='index'),
    path('trainer_result/',view=views.result, name='result')
]
