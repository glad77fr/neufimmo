from django.shortcuts import render
from django.http import HttpResponse
from .models import Promoteur, Programme
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .forms import ProgrammeForm


class Detail_view(DetailView):
    model = Programme
    template_name = 'monimmo/pages/detail_programme.html'

# Create your views here.
class SearchResultsView(ListView):
    model = Programme
    template_name = 'monimmo/pages/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Programme.objects.filter\
            (Q(nom__icontains=query))
        return object_list