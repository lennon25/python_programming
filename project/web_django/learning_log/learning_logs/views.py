from django.shortcuts import render

from .models import Topic

# Create your views here.


def index(request):
    return render(request, 'templates/index.html')


def topics(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'templates/topics.html', context)
