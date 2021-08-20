from django.urls import path
from django.views.generic import TemplateView
from .views import Detail_view, SearchResultsView, Subject_model_view
from .models import Programme

urlpatterns = [
    path('accueil/', TemplateView.as_view(template_name='monimmo/pages/accueil.html'), name='home'),
    path('search_result/', SearchResultsView.as_view(), name='search_results'),
    path('detail_programme/<slug:slug>/<int:pk>/', Detail_view.as_view(), name="detail_programme"),
    path('form_subject/', Subject_model_view.as_view(), name="create_subject")
]

