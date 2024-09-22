from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [  
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', views.like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', views.unlike_post, name='unlike_post')
]

urlpatterns += router.urls 