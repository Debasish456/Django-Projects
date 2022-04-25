from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('add_post',views.add_Post,name="add_post"),
    path('post/<str:pk>',views.post,name='post')
]
