from django.contrib import admin

from .models import Athlet, Page, CareerStage, AboutSection, Post, ContactData, Image, AthletImage, MyImage, PostTag, SocialMedia

class ImgAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['name', 'img_preview']

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview'] 
    fields = ['title', 'title_de', 'page', 'hero', 'img_preview', 'text', 'text_de']

class AthletsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'category']

class MyImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview'] 
    list_display = ['img_preview']

class AthletImageAdmin(admin.StackedInline):
    list_display = ['__str__', 'img_preview']
    readonly_fields = ['img_preview']
    model = AthletImage

class SocialMediaAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_preview']    
    list_display = ['__str__', 'icon_preview']

@admin.register(Athlet)
class AthletAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    inlines = [AthletImageAdmin]

    class Meta:
        model = Athlet

@admin.register(AthletImage)
class AthletsImageAdmin(admin.ModelAdmin):
    pass        

# Register your models here.

admin.site.register(MyImage, MyImageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(AboutSection)
admin.site.register(CareerStage)
admin.site.register(Post)
admin.site.register(ContactData)
admin.site.register(Image, ImgAdmin)
admin.site.register(PostTag)
admin.site.register(SocialMedia, SocialMediaAdmin)