from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView

from class_based import models
from django.urls import reverse_lazy

"""
def index(request):
    dict = {}
    return render(request, 'cbapp/index.html', context=dict)


class IndexView(View):
    def get(self, request):
        return HttpResponse('Hello World!')



class IndexView(TemplateView):
    template_name = 'cbapp/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['sample_text_1'] = 'Sample Text 1'
        contex['sample_text_2'] = 'Sample Text 2'
        return contex
"""


class IndexView(ListView):
    cotext_object_name = 'musician_list'
    model = models.Musician
    template_name = 'cbapp/index.html'


class MusicianDetails(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'cbapp/musician_details.html'


class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'cbapp/musician_form.html'


class UpdateMusician(UpdateView):
    fields = ('first_name','last_name', 'instrument')
    model = models.Musician
    template_name = 'cbapp/musician_form.html'


class DeleteMusician(DeleteView):
    cotext_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('cbapp:index')
    template_name = 'cbapp/delete_musician.html'