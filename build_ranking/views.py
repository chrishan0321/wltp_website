from django.shortcuts import render

# Create your views here.
def build_ranking_main(request):
	return render(request, "build_ranking/build_ranking.html")