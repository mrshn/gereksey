from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        (width, height) = img.size
          

        if height > 300 or width > 300 or height < 300 or width < 300:
            size = (300, 300)
            img = img.resize(size, Image.ANTIALIAS)
            img.save(self.image.path)
