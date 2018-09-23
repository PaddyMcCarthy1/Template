from django.db import models
from django.urls import reverse


# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def _get_absolute_url_(self):
        return reverse('property_detail', args=[str(self.id)])
