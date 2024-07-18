from django.db import models

# Create your models here.

class Note(models.Model):
    heading = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading[:30]