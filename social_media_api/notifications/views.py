from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def unread_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    data = [{'actor': n.actor.username, 'verb': n.verb, 'target': str(n.target), 'timestamp': n.timestamp} for n in notifications]
    return JsonResponse(data, safe=False)

# Create your views here.
