from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def download_report(request):
    return HttpResponse("This is a placeholder for the download report view.")

@csrf_exempt
def gitprofiler(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        url = request.POST.get('url')
        if url:  # Check if the URL is not None
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            page_contents = soup.prettify()
            return render(request, 'gitprofiler.html', {'username': username, 'page_contents': page_contents})
        else:
            return render(request, 'gitprofiler.html', {'username': username})
    else:
        return render(request, 'gitprofiler.html')

def scrape_job(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove script tags
    for script in soup.find_all('script'):
        script.decompose()

    data = {
        'title': soup.find('title').text if soup.find('title') else None,
        'h1': soup.find('h1').text if soup.find('h1') else None,
        'p': [p.text for p in soup.find_all('p')],
    }

    return data