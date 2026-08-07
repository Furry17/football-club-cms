from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Football Club CMS')
