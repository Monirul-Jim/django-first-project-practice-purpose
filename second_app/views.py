from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def second(request):
    if request.method == 'POST':
        form = forms.StudentModelForms(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponse("Form submitted successfully!")
    else:
        form = forms.StudentModelForms()
    return render(request, 'second_app/second.html', {'form': form})
