from django.shortcuts import render

def main_main(request):
	return render(request, "main/index.html")