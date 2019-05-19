"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

app_name = "econcs"
urlpatterns = [
    path('', views.to_home, name='to_home'),
    path('home', views.home, name='home'),
    path('people', views.people, name='people'),
    path('publication', views.publication, name='publication'),
    path('teaching', views.teaching, name='teaching'),
    path('seminar', views.seminar, name='seminar'),
    path('news', views.news, name='news'),
]
