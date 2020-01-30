from django.shortcuts import render

# Create your views here.
def index(request):
    e = 'https://www.amazon.com/'
    context = {
        'e': e
    }
    return render(request, 'test.html', context)
