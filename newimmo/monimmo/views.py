from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorations import have_reservation

from .models import Promoteur, Programme, Subject, Topic, Post, Reservation, Profile, User
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q
from .forms import SubjectModelForm, PostModelForm, SignUpForm, ReservationModelForm
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.avatar_img = form.cleaned_data.get('avatar_img')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


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
#@login_required(login_url="compte")
@have_reservation
def SubjectDetail(request,prog_pk, topic_slug, slug,sub_pk, post_slug):
    Prog = Programme.objects.get(pk=prog_pk)
    sub = Subject.objects.get(pk=sub_pk)
    posts = Post.objects.filter(subject=sub_pk)
    topic = Topic.objects.get(slug=topic_slug)
    x = Profile.objects.get(user=sub.user)

    return render(request, 'monimmo/pages/subjects_detail.html',
                  {"Subject":sub, "Posts":posts,"Programme":Prog, "active_topic" : topic, "x": x})

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

    def get_initial(self): # On va définir les valeurs par défaut
        initial = super().get_initial()
        initial["programme"] = self.kwargs['prog_pk']
        initial["user"] = self.request.user
        initial["topic"] =Topic.objects.get(slug=self.kwargs['topic_slug'])
        return initial

    def form_valid(self, form): # modifications après sauvegarde
        self.object = form.save(commit = False)
        self.object.topic = Topic.objects.get(slug=self.kwargs['topic_slug'])
        self.object.programme = Programme(pk=self.kwargs['prog_pk'])
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        topic = Topic.objects.get(slug=self.kwargs['topic_slug'])
        return reverse('sublist', kwargs={"prog_pk":self.kwargs['prog_pk'], "topic_slug" : self.kwargs['topic_slug'],
                                          "slug":self.kwargs["slug"]})

class Post_model_view(CreateView):
    model = Post
    template_name = "monimmo/forms/post_create.html"
    form_class = PostModelForm

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        initial["subject"] = self.kwargs["sub_pk"]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.subject = Subject(pk=self.kwargs["sub_pk"])
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Subject.objects.get(pk=self.kwargs["sub_pk"])
        context['Sujet'] = subject.title
        return context

    def get_success_url(self):
        return reverse('subdetail',kwargs={"slug": self.kwargs["slug"], "prog_pk":self.kwargs['prog_pk'], "topic_slug" : self.kwargs['topic_slug'],
                                          "post_slug": self.kwargs["post_slug"], "sub_pk": self.kwargs["sub_pk"]})

class post_reservation(CreateView):
    model = Reservation
    template_name = "monimmo/forms/create_reservation.html"
    form_class = ReservationModelForm

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        initial["programme"] = self.kwargs["prog_pk"]
        return initial

    def get_success_url(self):
        return reverse('detail_programme', kwargs={"slug" : self.kwargs["slug"], "pk" :self.kwargs["prog_pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        programme = Programme.objects.get(pk=self.kwargs["prog_pk"])
        context['programme_slug'] = programme.slug
        context['programme_pk'] = programme.pk
        context['programme_nom'] =programme.nom
        return context



