from django.shortcuts import render

# Create your views here.

def analysis_home(request):
    return render(request, 'app_home/analysis_home.html')