from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=1000, blank=True, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
