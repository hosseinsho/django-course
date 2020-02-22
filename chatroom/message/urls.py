from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
path('<int:user_id>', views.chatpage),
path('', views.chatpage),
path('add',views.add_message),

]