from django.shortcuts import render


def about(request):
    context = {
        'page': 'about',
    }
    return render(request, 'about/about.html', context)
