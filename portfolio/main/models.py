from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)  # or ManyToMany if advanced
    # image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    # created_date = models.DateField(auto_now_add=True)
    # etc.
    
    def __str__(self):
        return self.title
