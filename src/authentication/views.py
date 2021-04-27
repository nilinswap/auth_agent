from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def welcome(_request):
    return JsonResponse({"message": "Hi, what a nice day!"})
