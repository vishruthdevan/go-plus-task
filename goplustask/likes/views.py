from django.shortcuts import render
from django.http import HttpResponse
from .models import Stats
# Create your views here.


def index(request):
    context = {}
    if not Stats.objects.all():
        Stats.objects.create(likes=0, dislikes=0)
    else:
        context["likes"] = Stats.objects.all()[0].likes
        context["dislikes"] = Stats.objects.all()[0].dislikes
    return render(request, 'likes/index.html', context)
