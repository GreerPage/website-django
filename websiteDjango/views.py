from django.shortcuts import render
from django.shortcuts import redirect


def error_404(request, exception):
        data = {
            'error': 'Page Not Found',
            'errornum': '404',
            'linknum': '1',
        }
        return render(request,'error.html', data)

def error_500(request):
        data = {
            'error': 'Internal Server Error',
            'errornum': '500',
            'linknum': '1',
        }
        return render(request,'error.html', data)
def error_400(request, exception):
        data = {
            'error': 'Bad Request',
            'errornum': '400',
            'linknum': '1',
        }
        return render(request,'error.html', data)
def error_403(request, exception):
        data = {
            'error': 'Forbidden',
            'errornum': '403',
            'linknum': '1',
        }
        return render(request,'error.html', data)

