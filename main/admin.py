from django.contrib import admin
from main import models

# Register your models here.
admin.site.register(models.TodoList)
admin.site.register(models.Item)