# Create a basic form which will ask to fill basic details such as name, email and text.
# Create a basic form and perform form validation using in-built validator and our own custom validation.

from django.shortcuts import render
from . import forms


# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":  # someone hit submit and post it something back
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})
