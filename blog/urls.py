from django.urls import path, include
from .import views
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post-details/<slug:slug>/', views.post_details, name='post-details'),
]
