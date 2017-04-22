from django.shortcuts import render

# Create your views here.

def index(request):
    """ The learning Log Home Page."""
    return render(request, 'learning_logs/index.html')