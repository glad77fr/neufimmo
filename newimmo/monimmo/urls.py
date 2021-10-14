from django.urls import path
from django.views.generic import TemplateView
from .views import Detail_view, SearchResultsView, Subject_model_view, Topic_view, SubjectListView, SubjectDetail
from .models import Programme

urlpatterns = [
    path('accueil/', TemplateView.as_view(template_name='monimmo/pages/accueil.html'), name='home'),
    path('search_result/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/<int:pk>/', Detail_view.as_view(), name="detail_programme"),
    path('form_subject/', Subject_model_view.as_view(), name="create_subject"),
    path('<slug:slug>/<int:pk>/themes', Topic_view, name="consult_themes"),
    path('<slug:slug>/<int:prog_pk>/themes/<slug:topic_slug>/', SubjectListView, name='sublist'),
    path('<slug:slug>/<int:prog_pk>/themes/<slug:topic_slug>/<slug:post_slug>/<int:sub_pk>/', SubjectDetail, name="subdetail")
]

