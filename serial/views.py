from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'serial/main_page.html', {})


def register(request):
    return render(request, 'serial/register.html', {})
