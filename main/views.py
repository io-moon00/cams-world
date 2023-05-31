from django.shortcuts import render, get_object_or_404

from datetime import date
from .models import CareerStage, Page, AboutSection, Athlet, Post, AthletImage, MyImage, SocialMedia

# Create your views here.
current_year = date.today().year
all_athlets = Athlet.objects.filter(published = 'True')
social_media = SocialMedia.objects.all()


def home(request):
    page = Page.objects.get(page='home')
    return render(request, 'home.html', {'page': page, 'year': current_year, 'athlets': all_athlets, 'social_media': social_media})

def coaching(request):
    page = Page.objects.get(page='coaching')
    return render(request, 'coaching.html',{'page': page, 'year': current_year, 'athlets': all_athlets, 'social_media': social_media})    

def athlets(request):
    page = Page.objects.get(page='athlets')
    athlets_dt = Athlet.objects.filter(category='duathlon_triathlon', published = 'True')
    athlets_t = Athlet.objects.filter(category='triathlon', published = 'True')
    athlets_d = Athlet.objects.filter(category='duathlon', published = 'True')
    athlets_c = Athlet.objects.filter(category='cycling', published = 'True')
    return render(request, 'athlets.html',{'page': page, 'year': current_year, 'athlets': all_athlets, 'athlets_dt': athlets_dt, 'athlets_t': athlets_t, 'athlets_d': athlets_d, 'athlets_c': athlets_c, 'social_media': social_media})

def athlet(request, id):
    athlet = get_object_or_404(Athlet, pk=id)
    images = AthletImage.objects.filter(athlet=athlet)
    return render(request, 'athlet.html',{'year': current_year, 'athlets': all_athlets, 'athlet': athlet, 'images': images, 'social_media': social_media})    

def blog(request):
    page = Page.objects.get(page='blog')
    posts = Post.objects.filter(published = 'True')
    posts = posts.order_by('postDate')
    return render(request, 'blog.html',{'page': page, 'year': current_year, 'posts': posts, 'athlets': all_athlets, 'social_media': social_media})

def about(request):
    page = Page.objects.get(page='about')
    aboutSections = AboutSection.objects.all()
    careerStages = CareerStage.objects.all()
    images = MyImage.objects.all()
    return render(request, 'about.html', {'aboutSections': aboutSections, 'page': page, 'year': current_year, 'careerStages': careerStages, 'athlets': all_athlets, 'images': images, 'social_media': social_media})

def impressum(request):
    page = Page.objects.get(page='impressum')
    return render(request, 'impressum.html', {'page': page, 'year': current_year, 'athlets': all_athlets, 'social_media': social_media})

def legal(request):
    page = Page.objects.get(page='legal')
    return render(request, 'legal.html', {'page': page, 'year': current_year, 'athlets': all_athlets, 'social_media': social_media})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def page_not_found(request,):
    return render(request, '404.html')