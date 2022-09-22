from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Item(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=20)
    type = models.CharField(max_length=20)
    by = models.CharField(max_length=50, null=True)
    time = models.DateTimeField(blank=True, null=True)
    text = models.TextField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    descendants = models.IntegerField(default=0, null=True, blank=True)
    url = models.CharField(max_length=300, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    fetched = models.BooleanField(default=False)

    def __str__(self):
        name = f'{self.type} {self.id}'
        return name