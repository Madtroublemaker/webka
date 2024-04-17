import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Company, Vacancy


from .serializers import CompanySerializer, VacancySerializer


from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.decorators import APIView

from rest_framework import status, mixins, generics

class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class VacancyListView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer



class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer




@api_view(["GET"])
def company_vacancies(request, company_id):
    try:
        company = get_object_or_404(Company, id=company_id)
        vacancies = company.vacancy_set.all() 
        data = {
            'company': company.name,
            'vacancies': list(vacancies.values())
        }
        return Response(data)
    except Company.DoesNotExist:
        return Response({'error': 'Company does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def vacancy_top(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]  # Retrieve top ten vacancies by salary
    data = {
        'vacancies': list(vacancies.values())
    }
    return Response(data)