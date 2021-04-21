from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

app_name = 'feedhub'
urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='feed-dtl'),
    path('post/new/', PostCreateView.as_view(), name='feed-new'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='feed-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='feed-delete'),
    path('about/', views.about, name='feed-about'),
]
