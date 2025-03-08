from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)        # Searchable title  
    description = models.TextField()                # Searchable description
    technologies = models.CharField(max_length=200) # or ManyToMany if advanced. Searchable technologies
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)   # Images uploaded via /admin/
    # created_date = models.DateField(auto_now_add=True)
    # etc.
    
    def __str__(self):
        return self.title
