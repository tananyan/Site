from django.shortcuts import render


def index(request):
    return render(request, 'MainApp/homepage.html')


def contact(request):
    return render(request, 'MainApp/contact.html',
                  {'values': ['Звоните по телефону', 'boris@yandex.ru', '8(977)335-77-77']})

def registration(request):
    return render(request, 'MainApp/registration_form.html')