from django.db import models
from django.utils import timezone

class post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank = True,null = True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
