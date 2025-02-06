from django.shortcuts import render
from leaderboard.models import Player
# Create your views here.


def leaderboard_main(request):
    players = Player.objects.all().order_by("rank")
    context = {"players": players}
    return render(request, "leaderboard/leaderboard.html", context)