from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def projects(request):
    query = request.GET.get('q', None)
    # Once you have a Project model, filter based on `query`
    # projects = Project.objects.filter(...)
    return render(request, 'main/projects.html', {'projects': projects})