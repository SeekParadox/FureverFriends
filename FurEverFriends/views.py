from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template import loader
from .models import Breed

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def animal_option(request, animal_type):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            breeds = list(Breed.objects.get(animal=animal_type))
            return JsonResponse({'context': breeds})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

