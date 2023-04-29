from django.shortcuts import render

# Create your views here.
def user_defined_filter(request):
    d={'data':'How aRe yOu BaBy'}
    return render(request,'user_defined_filter.html',d)