from django.shortcuts import render
from learning_log.learning_logs.models import Topic

# Create your views here.

def index(request):
    """ The learning Log Home Page."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)