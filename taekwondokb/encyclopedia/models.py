from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Volume(models.Model):
    tom = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=250, default="Vol")
    slug = models.SlugField(null=True)
    original_file = models.FileField(upload_to='encyclopedia/toms')

    def __str__(self):
        return f"Том № {self.tom} {self.title}"
    
    def get_absolute_url(self):
        return reverse('encyclopedia:volume', kwargs={'volume':self.slug})
    


class Page(models.Model):
    tom = models.ForeignKey(Volume, on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    title = models.CharField(max_length=250, null=True,blank=True)
    text = RichTextUploadingField()
    is_last = models.BooleanField(default=False)
    def __str__(self):
        return f"Том № {self.tom.tom} сторінка {self.page}"
    
    def get_absolute_url(self):
        return reverse('encyclopedia:page', kwargs={'volume':self.tom.slug, 'page': self.page})