from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def single_politico(request, slug):
    return render(request, 'single-politico.html', {
        'politico_slug': slug
    })


def archive_politicos(request):
    return render(request, 'archive-politico.html')
