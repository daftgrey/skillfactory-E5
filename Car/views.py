from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q


class Home(ListView):
    model = Car
    template_name = 'Car/index.html'
    context_object_name = 'cars'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Garage collection'
        return context


class GetMan(ListView):
    model = Car
    template_name = 'Car/manufacturer.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(manufacturer__slug=self.kwargs['slug'])


class GetCar(DetailView):
    model = Car
    template_name = 'Car/single.html'
    context_object_name = 'car'


class Search(ListView):
    template_name = 'Car/search.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(
            Q(model__icontains=self.request.GET.get('s')) | Q(manufacturer__title__icontains=self.request.GET.get('s')))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def about_us(request):
    return render(request, 'Car/about_us.html')
