from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    photo = ImageField()
    testimonial = models.TextField()
    title = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name