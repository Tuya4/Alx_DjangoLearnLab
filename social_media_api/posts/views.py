from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset =Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)        

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post,
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
        return JsonResponse({'status': 'liked'}, status=201)
    else:
        return JsonResponse({'status': 'already liked'}, status=400)
    
@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
        return JsonResponse({'status': 'unliked'}, status=200)
    else:
        return JsonResponse({'status': 'not liked yet'}, status=400)
        