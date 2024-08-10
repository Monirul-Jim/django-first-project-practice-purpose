from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
# Create your views here.


def product(request):
    students = models.Students.objects.all()
    return render(request, 'first_app/product.html', {'data': students})


def delete_student(request, id):
    std = models.Students.objects.get(pk=id).delete()
    return redirect('/first-app/')
