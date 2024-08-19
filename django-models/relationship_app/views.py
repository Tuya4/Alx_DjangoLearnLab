from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'    

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid username or password'})
    return render(request, 'relationship_app/login.html')
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'    