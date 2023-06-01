from django.db import models
from datetime import date
from django.utils.html import mark_safe
from colorfield.fields import ColorField
# Create your models here.


POSITIONS = [
    ('center', 'Center'),
    ('top', 'Top'),
    ('bottom', 'Bottom'),
    ('left', 'Left'),
    ('right', 'Right'),
]

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    alt = models.CharField(max_length= 100)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')
    
    def __str__(self):
      return self.name

class Page(models.Model):
    title = models.CharField(max_length=50)
    title_de = models.CharField(max_length=50, blank=True)
    PAGES = [
    ('home', 'Home'),
    ('about', 'About me'),
    ('coaching', 'Coaching'),
    ('athlets', 'Athlets'),
    ('athlet', 'Single Athlet'),
    ('blog', 'Blog'),
    ('contact', 'Contact'),
    ('impressum', 'Impressum'),
    ('legal', 'Data protection'),
]
    page = models.CharField(max_length=20, choices=PAGES, default='home')
    hero = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')
    text = models.TextField(blank=True)
    text_de = models.TextField(blank=True)
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.hero.image.url}" width = "200"/>')

    def __str__(self):
        return self.title

class CareerStage(models.Model):
    year = models.CharField(max_length=12)
    text = models.TextField(max_length=255)
    text_de = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.text

class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    title_de = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    text_de = models.TextField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class Athlet(models.Model):
    published = models.BooleanField(default=True)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    CATEGORY = [
    ('duathlon', 'Duathlon'),
    ('duathlon_triathlon', 'Duathlon/Triathlon'),
    ('triathlon', 'Triathlon'),
    ('cycling', 'Cycling'),
]
    category = models.CharField(max_length=20, choices=CATEGORY, default='duathlon_triathlon')
    hero = models.ImageField(blank=True, upload_to='uploads/athlets/')
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.hero.url}" width = "200"/>')
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class AthletImage(models.Model):
    athlet = models.ForeignKey(Athlet, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/athlets/')
    image_alt = models.CharField(blank=True, max_length=40)
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')
    subtitle = models.CharField(max_length= 100, blank=True)
    subtitle_de = models.CharField(max_length= 100, blank=True)
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')

    def __str__(self):
        return "%s %s" % (self.athlet.first_name, self.athlet.last_name)

class MyImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    image_alt = models.CharField(blank=True, max_length=40)
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')
    subtitle = models.CharField(max_length= 100, blank=True)
    subtitle_de = models.CharField(max_length= 100, blank=True)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')

class PostTag(models.Model):
    COLOR_PALETTE = [
        ("#DB2828", "red", ),
        ("#fff12a", "yellow", ),
    ]
    color = ColorField(samples=COLOR_PALETTE, default = '#DB2828')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):  
    published = models.BooleanField(default=True)  
    title = models.CharField(max_length=50)
    title_de = models.CharField(max_length=50, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    subtitle_de = models.CharField(max_length=100, blank=True)
    tag= models.ForeignKey(PostTag, on_delete=models.CASCADE, null=True)
    postDate = models.DateField(default=date.today)
    content = models.TextField()
    content_de = models.TextField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')
    link = models.URLField(blank=True, null=True)
    link_text = models.CharField(blank=True, max_length=20)
    link_text_de = models.CharField(blank=True, max_length=20)
    def __str__(self):
        return self.title
    
class ContactData(models.Model):
    email = models.EmailField()
    phone_ch = models.CharField(max_length=20, blank=True)    
    phone_de = models.CharField(max_length=20, blank=True)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class SocialMedia(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='public/') 
    link = models.URLField()  

    class Meta:
        verbose_name_plural = "Social Media"

    def icon_preview(self): 
        return mark_safe(f'<img src = "{self.icon.url}" width = "50"/>')

    def __str__(self):
        return self.name

