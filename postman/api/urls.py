from django.urls import path
from .views import CompanyListView, CompanyDetailView, VacancyListView, VacancyDetailView, company_vacancies, vacancy_top

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/top_ten', vacancy_top),
]