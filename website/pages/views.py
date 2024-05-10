from django.shortcuts import render
from dataset.models import DatasetEntry

def landing_page(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

def resources(request):
    return render(request, 'resources.html')

def dataset_view(request):
    entries = DatasetEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'dataset.html', context)