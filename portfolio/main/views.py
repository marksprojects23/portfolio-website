from django.shortcuts import render                                         # `render` library so the views can render things
from .models import Project                                                 # Bringing in Project objects to be queried

# Create your views here.
def home(request):                                                          # This view function will
    return render(request, 'main/home.html')                                # display the home page

def projects(request):
    query = request.GET.get('q', None)
    if query:                                                               # If the query matches the title or description or technology, display it
        projects = Project.objects.filter(title__icontains=query) | Project.objects.filter(description__icontains=query) | Project.objects.filter(technologies__icontains=query)
    else:
        projects = Project.objects.all()                                    # Shows all projects if nothing is in search bar
    return render(request, 'main/projects.html', {'projects': projects})