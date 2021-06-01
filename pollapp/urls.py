from django.contrib import admin
from django.urls import path, include
from . import views
from pollapp  import views as poll_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Index, name = 'Index'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]



