"""
URL configuration for joli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get('/hello')
def hello(request) -> dict:
    return {'response':'Hello'}

@api.get('/add')
def addition(request, a: int | float, b: int | float) -> dict:
    return {'result': a + b}

@api.get('/subtract')
def subtract(request,a: int | float, b: int | float) -> dict:
    return {'result': a - b}

@api.get('/multiply')
def multiply(request, a: int | float, b: int | float) -> dict:
    return {'result': a * b}

@api.get('/divide')
def divide(request, a: int | float, b: int | float) -> dict:
    if b == 0:
        return {'Error':'Zero Division Error.'}
    else:
        return {'Result': a / b}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
