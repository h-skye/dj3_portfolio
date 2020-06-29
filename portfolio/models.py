from django.db import models

class Project(models.Model):
    title = models.Charfield(max_length=100)
    description = models.Charfield(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
