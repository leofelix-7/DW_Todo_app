from django.contrib import admin
from .models import TodoModel, Tag
# Register your models here.

admin.site.register(TodoModel)
admin.site.register(Tag)
