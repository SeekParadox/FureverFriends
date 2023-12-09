from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template import loader


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())



