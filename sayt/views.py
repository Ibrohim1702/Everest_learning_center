from django.shortcuts import render

from sayt.models import Subscribe


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "index.html", ctx)

def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)

def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)

def services(requests):
    ctx = {

    }
    return render(requests, "services.html", ctx)

def blog(requests):
    ctx = {

    }
    return render(requests, "blog.html", ctx)


