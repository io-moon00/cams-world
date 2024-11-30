from django.contrib import admin
from .models import Athlete, Page, CareerStage, Post, ContactData, Image, AthleteImage, MyImage, PostTag, SocialMedia
from adminsortable2.admin import SortableAdminMixin

class ImgAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['name', 'img_preview']

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview'] 
    fields = ['page', 'title', 'title_de', 'hero', 'position', 'img_preview', 'text', 'text_de']
    list_display = ['page', 'title']

class MyImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['img_preview', 'ordering']
    readonly_fields = ['img_preview']
    ordering = ['ordering']

class AthleteImageInline(admin.StackedInline):
    model = AthleteImage
    extra = 1
    readonly_fields = ['img_preview']
    fields = ['img_preview', 'image', 'image_alt', 'position', 'subtitle', 'subtitle_de']

class AthletesAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'category', 'published']
    inlines = [AthleteImageInline]

class CareerStageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'year']

class SocialMediaAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']    
    list_display = ['__str__', 'icon_preview']

class PostTagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'color_display']

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'postDate', 'published']
    list_filter = ['postDate', 'published']

# Register your models here.
admin.site.register(MyImage, MyImageAdmin)
admin.site.register(Athlete, AthletesAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(CareerStage, CareerStageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ContactData)
admin.site.register(Image, ImgAdmin)
admin.site.register(PostTag, PostTagAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)