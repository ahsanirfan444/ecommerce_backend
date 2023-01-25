import uuid

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.FloatField()
    category = models.CharField(max_length=225)
    description = models.TextField()    
    instock = models.BooleanField(default=True)
    offer_badge = models.BooleanField(default=False)
    popular_items = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=False)
    width_field = models.IntegerField(default=200)
    height_field = models.IntegerField(default=200)
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True,
                              width_field='width_field',
                              height_field='height_field',)

    def __str__(self):
        return f'{self.slug} | {self.id}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

