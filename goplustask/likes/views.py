from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def like(request):
    if not Stats.objects.all():
        Stats.objects.create(likes=0, dislikes=0)
    else:
        s = Stats.objects.all()[0]
        s.likes = request.POST["likes"]
        s.save()
    return JsonResponse({"likes": Stats.objects.all()[0].likes})


@csrf_exempt
def dislike(request):
    if not Stats.objects.all():
        Stats.objects.create(likes=0, dislikes=0)
    else:
        s = Stats.objects.all()[0]
        s.dislikes = request.POST["dislikes"]
        s.save()
    return JsonResponse({"dislikes": Stats.objects.all()[0].dislikes})
