from django.urls import path, include
from .import views
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post-details/<slug:slug>/', views.post_details, name='post-details'),
    path('share-post/<str:pk>', views.share_post, name='share-post'),
    path('create-comment/<str:pk>/', views.create_comment, name='create-comment'),
    path('user-login/', views.user_login, name='user-login'),
    path('user-logout/',  views.user_logout, name='user-logout'),
    path('create-user/', views.create_user, name='create-user'),
]
