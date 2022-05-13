from django.db import models

# Create your models here.

class Cake(models.Model):
    name = models.CharField('Cake name', max_length=200)
    about = models.TextField('Cake about')
    img = models.ImageField('Cake img', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cake'
        verbose_name_plural = 'Cakes'

class AboutSite(models.Model):
    name = models.CharField('About name', max_length=200)
    about = models.TextField('About about')
    img = models.ImageField('About Img', upload_to='media')

    def __str__(self):
        return self.name
