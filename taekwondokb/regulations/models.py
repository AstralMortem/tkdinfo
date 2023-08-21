from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Belt(models.Model):
    kup = models.CharField(max_length=30)
    kupslug = models.SlugField(primary_key=True, unique=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='regulations/belts')

    def __str__(self):
        return self.title + f"({self.kup})"
    
    def get_image(self):
        return self.image.url
    
    def get_absolute_url(self):
        return reverse('regulations:regulation', kwargs={'belt_kup': self.kupslug})
    

class Regulation(models.Model):
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)
    description = RichTextField()
    tul = RichTextField()
    kicks = RichTextField()
    sparings = RichTextField(null=True, blank=True)
    self_defence = RichTextField(null=True, blank=True)
    spec_tech = RichTextField(null=True, blank=True)
    power_kicks = RichTextField(null=True, blank=True)
    OFP = RichTextField()
    theory = RichTextField(null=True, blank=True)

    def __str__(self):
        return str(self.belt)
    
    def get_image(self):
        return self.belt.get_image()
    
    def get_absolute_url(self):
        return reverse('regulations:regulation', kwargs={'belt_kup': self.belt.kupslug})
