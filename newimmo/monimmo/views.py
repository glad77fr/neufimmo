from django.shortcuts import render
from django.http import HttpResponse
from .models import Promoteur, Programme, Subject
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q
from .forms import SubjectModelForm


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

class Subject_model_view(CreateView):
    model = Subject
    template_name = "monimmo/forms/Subject_post.html"
    form_class = SubjectModelForm


