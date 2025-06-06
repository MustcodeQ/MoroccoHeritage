"""
URL configuration for moroccoVibe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.morocco_view, name='base'),  # default page
    path('about/', views.about_view, name='about'),
    path('culture/', views.culture_view, name='culture'),
    path('holidays/', views.holidays_view, name='holidays'),
    path('morocco/', views.morocco_view, name='morocco'),
    path('family', views.family_view, name='family'),
    path('contact', views.contact_view, name='contact'),
]
