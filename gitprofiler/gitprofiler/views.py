from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ButtonPress

def download_report(request):
    return HttpResponse("This is a placeholder for the download report view.")

@csrf_exempt
def gitprofiler(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        url = request.POST.get('url')
        if username and url:  # Check if the username and URL are not None
            button_press = ButtonPress(username=username, url=url)
            button_press.save()
        return render(request, 'gitprofiler.html')
    else:
        return render(request, 'gitprofiler.html')