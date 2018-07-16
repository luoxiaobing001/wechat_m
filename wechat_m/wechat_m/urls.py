"""wechat_m URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('login/',  views.login, name='login'),
    path('province/', views.getProvince),
    path('city/<int:pid>/', views.getCity),
    path('county/<int:cid>/', views.getCounty),
    path('department/', views.getDepartment),
    path('position/', views.getPosition),
    # path('chart/', views.chart, name='chart'),
    path('modify/', views.modify, name='modify'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout, name='logout'),

    path('personal/', views.personal_week_chart, name='personal'),
    path('group/', views.group_week_chart, name='group'),
    path('people/', views.people_day_chart, name='people'),
]
