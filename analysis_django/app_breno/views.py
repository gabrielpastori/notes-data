from django.shortcuts import render

# Create your views here.

def analysis_breno(request):
    return render(request, 'app_breno/analysis_breno.html')