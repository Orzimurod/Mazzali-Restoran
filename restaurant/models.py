from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hero/')

    def __str__(self):
        return self.title
    

from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slider/')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starters', 'Yengil taom'),
        ('salads', 'Salatlar'),
        ('soft drink', 'Ichimliklar'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chefs/')

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=100, null=True, blank=True) 
    def __str__(self):
        return self.title


# class Contact(models.Model):
#     name = models.CharField(max_length=100)  # Foydalanuvchi ismi
#     email = models.EmailField()  # Elektron pochta
#     subject = models.CharField(max_length=200)  # Mavzu
#     message = models.TextField()  # Xabar

#     def __str__(self):
#         return self.subject

