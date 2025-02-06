from django.shortcuts import render

# Create your views here.
def description_main(request):
    return render(request, "description/description.html")
