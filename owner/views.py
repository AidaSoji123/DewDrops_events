from django.shortcuts import render
from .models import EventCategory
# Create your views here.
# views.py



def index(request):
    event_categories = EventCategory.objects.all()
    return render(request, 'index.html', {'event_categories': event_categories})


def home(request):
    return render(request, 'owner/index.html')

def inner_page(request):
    return render(request, 'owner/inner-page.html')

