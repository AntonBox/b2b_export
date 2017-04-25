from django.db import models
from root.base_models import TimedModel

from datetime import datetime


def get_image_path(instance, filename):
    return 'products_img/{0}/{1}/{2}/{3}'.format(datetime.now().year,
                                                 datetime.now().month,
                                                 datetime.now().day,
                                                 filename)


class Product (TimedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image1 = models.ImageField(upload_to=get_image_path)
    image2 = models.ImageField(upload_to=get_image_path)
    image3 = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return self.name
