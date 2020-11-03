from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from link.forms import SpecificationCreateForm
from link.models import Specification


def index(request):
    return render(request, 'index.html')


def edo(request):
    return render(request, 'edo.html')


def ofd(request):
    return render(request, 'ofd.html')


def mark(request):
    return render(request, 'mark.html')


class SpecificationCreateView(generic.CreateView):
    model = Specification
    template_name = 'specification_create.html'
    form_class = SpecificationCreateForm
    success_url = reverse_lazy('index')
