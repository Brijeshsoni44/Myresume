from django.shortcuts import render, redirect
from core.models import Contact

# Create your views here.
def home(request):
    context = {'home' : 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['msg']
        print(name, email, subject, msg)
        contact = Contact(name=name, email= email, subject=subject, msg= msg)
        contact.save()


    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)
