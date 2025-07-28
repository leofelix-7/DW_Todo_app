from django.db import models
from colorfield.fields import ColorField
import uuid
from django.core.exceptions import ValidationError

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True) 
    color = ColorField(default="#0099FF") 

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError({'name': "Tag name must be at least 2 characters long."})
        super().clean()

    def __str__(self):
        return self.name

class TodoModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', related_name='todos', blank=True) # added
    date = models.DateField(null=True, blank=True) # added
    time = models.TimeField(null=True, blank=True) # added

    def __str__(self):
        return self.title