from django.urls import path 

from . import views


app_name = 'blog'

urlpatterns = [
    path('' ,views.post_list , name='post_list'),
    path('<int:id>' ,views.post_detail , name='post_detail'),
    path('<int:id>/edit' ,views.post_update , name='post_update'),
    path('create' , views.post_create , name='post_create')
]