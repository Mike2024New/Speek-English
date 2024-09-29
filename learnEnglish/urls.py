from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls',namespace='main')),
    path('',include('phrase_loader.urls',namespace='phrase_loader')),
    path('',include('trainer.urls',namespace='trainer')),
]
