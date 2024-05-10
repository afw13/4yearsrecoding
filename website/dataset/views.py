from django.shortcuts import render
from .models import DatasetEntry

def dataset_view(request):
    entries = DatasetEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'dataset/dataset.html', context)