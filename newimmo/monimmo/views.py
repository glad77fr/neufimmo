from django.shortcuts import render
from django.http import HttpResponse
from .models import Promoteur, Programme, Subject, Topic, Post
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q
from .forms import SubjectModelForm
from django.shortcuts import render


class Detail_view(DetailView):
    model = Programme
    template_name = 'monimmo/pages/detail_programme.html'

def Topic_view(request, slug, pk ):
    Topic_display = Topic.objects.all()
    list_subcount = []
    for topic in Topic.objects.all():
        list_subcount.append(len(Subject.objects.filter(programme=pk,topic=topic.pk)))
    dict_context = {}
    dict_context["Topics"] = zip(Topic_display, list_subcount)
    dict_context["Programme"] = Programme.objects.get(pk=pk)
    return render(request, 'monimmo/pages/themes.html', dict_context)

def SubjectListView(request, prog_pk, topic_slug, slug):
    Prog = Programme.objects.get(pk=prog_pk)
    topic = Topic.objects.get(slug=topic_slug)
    List_Sub = Subject.objects.filter(programme=prog_pk, topic=topic.pk)
    list_post = []
    for sub in Subject.objects.filter(programme=prog_pk, topic=topic.pk):
        list_post.append(len(Post.objects.filter(subject=sub.pk)))
    return render(request, 'monimmo/pages/subjects.html', {"Sub_List":List_Sub, "Programme":Prog,
                                                           "topic" : zip(List_Sub, list_post), "test":list_post, "active_topic" : topic})

def SubjectDetail(request,prog_pk, topic_slug, slug,sub_pk, post_slug):
    Prog = Programme.objects.get(pk=prog_pk)
    sub = Subject.objects.get(pk=sub_pk)
    posts = Post.objects.filter(subject=sub_pk)
    topic = Topic.objects.get(slug=topic_slug)

    return render(request, 'monimmo/pages/subjects_detail.html',
                  {"Subject":sub, "Posts":posts,"Programme":Prog, "active_topic" : topic })

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
    template_name = "monimmo/forms/subject_post.html"
    form_class = SubjectModelForm

    def get_initial(self):
        initial = super().get_initial()
        # initial["content"] = self.request.GET.get('prog_pk')
        initial["programme"] = self.kwargs['prog_pk']

        # print(self.request.GET.get('prog_pk'))
            # self.request.GET.get('prog_pk')
        return initial

    # def form_valid(self, form):
    #     form.instance.programme = self.request.prog_pk
    #     return super().form_valid(form)





