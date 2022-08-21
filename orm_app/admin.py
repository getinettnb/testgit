from django.contrib import admin

# Register your models here.

from .models import Room, Project,Topic,message

admin.site.register(Room)
admin.site.register(Project)
admin.site.register(Topic)
admin.site.register(message)
