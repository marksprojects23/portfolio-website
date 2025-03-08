from django.contrib import admin
from .models import Project         # So we can edit project items through the admin panel

# Register your models here.
admin.site.register(Project)