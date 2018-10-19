from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
]
