from django.http import HttpResponse
from django.shortcuts import render
from .forms import ItemRequestForm


# Create your views here.
def index(request):
    invalid = False

    if request.method == 'POST':
        form = ItemRequestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            invalid = True

    form = ItemRequestForm()

    return render(request, 'index.xhtml', {'form': form, 'invalid': invalid})
