from django.shortcuts import render

def Home(request):
    template = 'Root/index.html'
    return render(request,template)