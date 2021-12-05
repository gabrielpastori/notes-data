from django.shortcuts import render

# Create your views here.

def analysis_cleomar(request):
    return render(request, 'app_cleomar/analysis_cleomar.html')