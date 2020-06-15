from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.post_list, name='home'),
    path('post/<str:category_name>/', views.post_list, name='post_list'),
    path('post/details/<int:post_id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
]