from django.utils import path 
from . models import Post 


app_name = 'blog'  #a namespace used to organize our urls by application
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]