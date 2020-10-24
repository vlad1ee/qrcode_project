from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def edo(request):
    return render(request, 'edo.html')

def ofd(request):
    return render(request, 'ofd.html')

def mark(request):
    return render(request, 'mark.html')