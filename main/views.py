from django.shortcuts import render
from .models import slide

# Create your views here.
def home(request):
    slides = slide.objects.all()
    return render(request, 'carousel/home.html', {'slides': slides})