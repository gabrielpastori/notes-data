from django.shortcuts import render

# Create your views here.

def analysis_gabriel(request):
    return render(request, 'app_gabriel/analysis_gabriel.html')