from django.db import models
from datetime import date
from django.utils.html import mark_safe
from colorfield.fields import ColorField
from django_ckeditor_5.fields import CKEditor5Field

import os

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
    alt = models.CharField(max_length= 100, help_text="Add an alternative text for the image. This text will be displayed when the image could not be loaded.", verbose_name="Alternative Text for Image")

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')
    
    def delete(self, *args, **kwargs):
        # Delete the image file from the file system
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        # Call the superclass delete method
        super().delete(*args, **kwargs)
    
    def __str__(self):
      return self.name

class Page(models.Model):
    title = models.CharField(max_length=50)
    title_de = models.CharField(max_length=50, blank=True, help_text="Enter the title for the german version of the page.")
    PAGES = [
    ('home', 'Home'),
    ('about', 'About me'),
    ('coaching', 'Coaching'),
    ('athletes', 'Athletes'),
    ('blog', 'Blog'),
    ('contact', 'Contact'),
    ('impressum', 'Impressum'),
    ('legal', 'Data protection'),
]
    page = models.CharField(max_length=20, choices=PAGES, default='home')
    hero = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, help_text='Select image to be displayed at the top of the page as the hero image.')
    position = models.CharField(max_length=20, choices=POSITIONS, default='center', help_text="Determines how the image is aligned within its frame.", verbose_name="Image Position")
    text = CKEditor5Field('Content', config_name='extends', blank=True)
    text_de = CKEditor5Field('Content german', config_name='extends', blank=True)
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.hero.image.url}" width = "200"/>')

    def __str__(self):
        return self.title

class CareerStage(models.Model):
    year = models.CharField(max_length=12)
    title = models.CharField(max_length=100)
    title_de = models.CharField(max_length=100, blank=True)
    text = models.TextField(max_length=255, blank=True)
    text_de = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Races/Teams"
        verbose_name = "Race/Team"

    def __str__(self):
        return self.title

class Athlete(models.Model):
    published = models.BooleanField(default=True, help_text="If checked, this athlete will be published on the website.")  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    content = CKEditor5Field('Content', config_name='extends', blank=True)
    content_de = CKEditor5Field('Content german', config_name='extends', blank=True)
    CATEGORY = [
    ('duathlon', 'Duathlon'),
    ('duathlon_triathlon', 'Duathlon/Triathlon'),
    ('triathlon', 'Triathlon'),
    ('cycling', 'Cycling'),
]
    category = models.CharField(max_length=20, choices=CATEGORY, default='duathlon_triathlon')
    hero_img = models.ImageField(blank=True, upload_to='uploads/athlets/', verbose_name="Hero Image")
    position = models.CharField(max_length=20, choices=POSITIONS, default='center', verbose_name="Hero Position")

    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk:
            # Get the existing instance from the database
            existing_instance = Athlete.objects.get(pk=self.pk)
            # Check if the hero_img has changed
            if existing_instance.hero_img != self.hero_img:
                # Delete the old image file if it exists
                if existing_instance.hero_img and os.path.isfile(existing_instance.hero_img.path):
                    os.remove(existing_instance.hero_img.path)

        # Check for any files with the same name in the directory and delete them
        if self.hero_img:
            hero_img_path = self.hero_img.path
            hero_img_name = os.path.basename(hero_img_path)
            directory = os.path.dirname(hero_img_path)
            for filename in os.listdir(directory):
                if filename == hero_img_name:
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)

        super().save(*args, **kwargs)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.hero_img.url}" width = "200"/>')
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class AthleteImage(models.Model):
    athlete = models.ForeignKey(Athlete, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/athlets/')
    image_alt = models.CharField(blank=True, max_length=40, verbose_name="Alternative Text for Image", help_text="Add an alternative text for the image. This text will be displayed when the image could not be loaded.")
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')
    subtitle = models.CharField(max_length= 100, blank=True)
    subtitle_de = models.CharField(max_length= 100, blank=True)

    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk:
            # Get the existing instance from the database
            existing_instance = Athlete.objects.get(pk=self.pk)
            # Check if the hero_img has changed
            if existing_instance.hero_img != self.image:
                # Delete the old image file if it exists
                if existing_instance.hero_img and os.path.isfile(existing_instance.hero_img.path):
                    os.remove(existing_instance.hero_img.path)
        
        super().save(*args, **kwargs)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')

    def __str__(self):
        return "%s %s" % (self.athlete.first_name, self.athlete.last_name)

class MyImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    image_alt = models.CharField(blank=True, max_length=40)
    position = models.CharField(max_length=20, choices=POSITIONS, default='center')
    subtitle = models.CharField(max_length= 100, blank=True)
    subtitle_de = models.CharField(max_length= 100, blank=True)
    ordering = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['ordering']

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}" width = "200"/>')

class PostTag(models.Model):
    COLOR_PALETTE = [
        ("#DB2828", "red", ),
        ("#fff12a", "yellow", ),
    ]
    color = ColorField(samples=COLOR_PALETTE, default = '#DB2828')
    name = models.CharField(max_length=20)

    def color_display(self):
        return mark_safe(f'<div style="width: 20px; height: 20px; background-color: {self.color};"></div>')
    color_display.short_description = 'Color'

    def __str__(self):
        return self.name


class Post(models.Model):  
    published = models.BooleanField(default=True, help_text="If checked, this post will be published on the website.")  
    title = models.CharField(max_length=50)
    title_de = models.CharField(max_length=50, blank=True, help_text="Enter the title for the German version of the website.")
    tag= models.ForeignKey(PostTag, on_delete=models.CASCADE)
    postDate = models.DateField(default=date.today, verbose_name="Post Date")
    content = CKEditor5Field('Content', config_name='extends')
    content_de = CKEditor5Field('Content german', config_name='extends')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, help_text='Select the image to be displayed at the top of the page as the hero image.')
    position = models.CharField(max_length=20, choices=POSITIONS, default='center', help_text="Determines how the image is aligned within its frame.", verbose_name="Image Position")

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

    def __str__(self):
        return 'Email and Phone'

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

