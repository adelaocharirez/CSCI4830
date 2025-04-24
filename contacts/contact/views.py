from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from django.db import models

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/index.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact/add_contact.html', {'form': form})

def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/edit_contact.html', {'form': form, 'contact': contact})

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('index')

def search_contact(request):
    query = request.GET.get('query', '')
    contacts = Contact.objects.filter(
        models.Q(name__icontains=query) |
        models.Q(email__icontains=query)
    )
    return render(request, 'contact/search_results.html', {'contacts': contacts, 'query': query})
