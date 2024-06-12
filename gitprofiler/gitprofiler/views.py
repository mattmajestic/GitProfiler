from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ButtonPress, Neon

def add_row(request):
    # Create a new instance of the Neon model
    new_neon = Neon()

    # Save the instance, which will add a new row to the Neon table
    new_neon.save()

    return HttpResponse("Row added successfully")

def download_report(request):
    return HttpResponse("This is a placeholder for the download report view.")

@csrf_exempt
def gitprofiler(request):
    # Create a new instance of the Neon model
    new_neon = Neon()

    # Save the instance, which will add a new row to the Neon table
    new_neon.save()

    if request.method == 'POST':
        username = request.POST.get('username')
        url = request.POST.get('url')
        if username and url:  # Check if the username and URL are not None
            button_press = ButtonPress(username=username, url=url)
            button_press.save()
        return render(request, 'gitprofiler.html')
    else:
        return render(request, 'gitprofiler.html')