from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from PIL import Image
from .choices import *
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=20)
    mini_content = models.CharField(default="", max_length=100)
    content = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="ilan_resmi")
    Kategori_1 = models.IntegerField(choices=RELEVANCE_CHOICES, default=1)
    Kategori_2 = models.IntegerField(choices=STATUS_CHOICES, default=1)
    iletisim = models.CharField(default="", max_length=100)
    Aktiflik = models.IntegerField(choices=AKTIF_CHOICES, default=1)

    
    def __str__(self):
        return self.title
    
    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        (width, height) = img.size
          

        if height > 300 or width > 300 or height < 300 or width < 300:
            size = (300, 300)
            img = img.resize(size, Image.ANTIALIAS)
            img.save(self.image.path)
        

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
