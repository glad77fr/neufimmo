from django.urls import path, include
from django.contrib.auth import views
from django.views.generic import TemplateView
from .views import Detail_view, SearchResultsView, Subject_model_view, Topic_view, SubjectListView, SubjectDetail, Post_model_view, signup,post_reservation
from .models import Programme

urlpatterns = [
    path('accueil/', TemplateView.as_view(template_name='monimmo/pages/accueil.html'), name='home'),
    path(r'signup/', signup, name='signup'),
    path('compte/', TemplateView.as_view(template_name='registration/compte.html'), name='compte'),
    path(r"accounts/", include("django.contrib.auth.urls")),
    path('search_result/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/<int:pk>/', Detail_view.as_view(), name="detail_programme"),
    path('<slug:slug>/<int:prog_pk>/themes/<slug:topic_slug>/form_subject/', Subject_model_view.as_view(), name="create_subject"),
    path('<slug:slug>/<int:pk>/themes', Topic_view, name="consult_themes"),
    path('<slug:slug>/<int:prog_pk>/themes/<slug:topic_slug>/', SubjectListView, name='sublist'),
    path('<slug:slug>/<int:prog_pk>/themes/<slug:topic_slug>/<slug:post_slug>/<int:sub_pk>/', SubjectDetail, name="subdetail"),
    path('<slug:slug>/<int:prog_pk>/themes/<slug:topic_slug>/<slug:post_slug>/<int:sub_pk>/post_reply/', Post_model_view.as_view(), name="post_reply"),
    path('<slug:slug>/<int:prog_pk>/reservation/',post_reservation.as_view() , name="reservation")
]

