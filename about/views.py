from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    
    if request.method == 'POST':
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, 'Thank you for reaching out! We will get back to you soon.')
    
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {'about': about,
         "collaborate_form": collaborate_form,},
    )
