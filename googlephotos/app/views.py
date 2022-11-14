from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def slide(request):
    return render(request,'movie.html')

def slide2(request):
    return render(request,'video.html')