from django.shortcuts import render

# Create your views here.
def rule_main(request):
	return render(request, "rule/index.html")
