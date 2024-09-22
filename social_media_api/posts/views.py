from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()
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
    
# @login_required
# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     user = request.user
#     like, created = Like.objects.get_or_create(user=request.user, post=post)
#     if created:
#         Notification.objects.create(
#             recipient=post.author,
#             actor=request.user,
#             verb='liked your post',
#             target=post,
#             target_content_type=ContentType.objects.get_for_model(post),
#             target_object_id=post.id
#         )
#         return JsonResponse({'status': 'Post liked'}, status=201)
#     else:
#         return JsonResponse({'status': 'already liked'}, status=400)
    
# @login_required
# def unlike_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     like = Like.objects.filter(user=request.user, post=post).first()
#     if like:
#         like.delete()
#         return JsonResponse({'status': 'unliked'}, status=200)
#     else:
#         return JsonResponse({'status': 'not liked yet'}, status=400)
        
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Use generics.get_object_or_404 instead of shortcuts.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Check if the post is already liked by the user
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "Post already liked"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new like entry
        Like.objects.create(user=user, post=post)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post
        )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        # Use generics.get_object_or_404 instead of shortcuts.get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the like exists
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the like
        like.delete()

        return Response({"detail": "Post unliked"}, status=status.HTTP_204_NO_CONTENT)        