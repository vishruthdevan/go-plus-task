from django.shortcuts import render
from django.http import JsonResponse
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


def like(request):
    if not Stats.objects.all():
        Stats.objects.create(likes=0, dislikes=0)
    else:
        Stats.objects.all()[0].likes += 1
        Stats.objects.all()[0].save()
    return JsonResponse({"likes": Stats.objects.all()[0].likes})


def dislike(request):
    if not Stats.objects.all():
        Stats.objects.create(likes=0, dislikes=0)
    else:
        Stats.objects.all()[0].dislikes += 1
        Stats.objects.all()[0].save()
    return JsonResponse({"dislikes": Stats.objects.all()[0].dislikes})
