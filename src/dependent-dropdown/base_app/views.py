from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.edit import BaseCreateView
from .models import Person, City
from .forms import PersonForm

def home(request):
    return render(request, 'home.html', {})


class AddPerson(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'add_person.html'

    def get_success_message(self, cleaned_data):
        return f"{cleaned_data['name']} insrted into table"


class PersonList(ListView):
    model = Person
    queryset = Person.objects.order_by('-id')
    template_name = 'person_list.html'
    context_object_name = 'persons'


class UpdatePerson(SuccessMessageMixin, UpdateView):
    model = Person
    queryset = Person.objects.all()
    template_name = 'add_person.html'
    form_class = PersonForm
    success_message = "Updated Successfully"


def delete_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        person.delete()
        messages.success(request, "Person deleted from database")
        return redirect('base_app:person-list')
    except ObjectDoesNotExist:
        messages.warning(request, "No such person exists")
        return redirect('base_app:person-list')


def get_city_by_country_id(request, pk):
    cities = list(City.objects.filter(country__id=pk).values())
    return JsonResponse(cities, safe=False)


def autocomplete(request):
    if request.is_ajax():
        query = request.GET.get("term", "")
        qs = Person.objects.filter(name__icontains=query)
        return JsonResponse("ok", safe=False)
    return render(request, 'autocomplete.html', {})
    # return JsonResponse("ok", safe=False)