from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.template import loader
from .models import Breed


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def pet_search(request):
    location = request.GET.get('Location')
    breed = request.GET.get('breed')
    age = request.GET.get('age')
    if not (location and breed and age):
        return HttpResponseBadRequest('Invalid request parameters', status=400)
    print(request.GET.values())
    print(location, breed, age)
    template = loader.get_template('pet-search.html')
    return HttpResponse(template.render())


def animal_option(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    animal = request.GET.get('animal')

    if is_ajax and animal:
        if request.method == 'GET':
            breeds = list(Breed.objects.filter(animal=animal).values())
            return JsonResponse({'context': breeds})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request', status=400)
