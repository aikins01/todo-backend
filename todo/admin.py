from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'date_created','due_date', 'priority',)

# Register your models here.

admin.site.register(Todo, TodoAdmin)