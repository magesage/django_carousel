from django.db import models

# Create your models here.
class slide(models.Model):
    url = models.ImageField(upload_to='slides/')
    caption = models.CharField(max_length=255)
    alt = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption