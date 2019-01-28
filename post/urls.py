from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/update', views.update, name='update'),
    path('<int:post_id>/addcomment', views.addcomment, name='addcomment'),
]
