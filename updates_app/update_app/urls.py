from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_page,name='index'),
    path('posts/<str:pk>',views.posts_page,name='posts'),
]