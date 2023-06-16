from django.contrib import admin
from django.urls import path, include
import sinais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sinais.urls')),
]
