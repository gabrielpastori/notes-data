from django.shortcuts import render

# Create your views here.

def analysis_gustavo(request):
    return render(request, 'app_gustavo/analysis_gustavo.html')