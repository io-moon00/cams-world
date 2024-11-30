from django.shortcuts import render, get_object_or_404
from django.db.models import IntegerField
from django.db.models.functions import Cast
from datetime import date
from .models import CareerStage, Page, Athlete, Post, AthleteImage, MyImage, SocialMedia


def home(request):
    page = Page.objects.get(page='home')
    return render(request, 'home.html', {'page': page})

def coaching(request):
    page = Page.objects.get(page='coaching')
    return render(request, 'coaching.html',{'page': page})    

def athletes(request):
    page = Page.objects.get(page='athletes')
    return render(request, 'athletes.html',{'page': page})

def athlete(request, id):
    athlete = get_object_or_404(Athlete, pk=id)
    images = AthleteImage.objects.filter(athlete=athlete)
    return render(request, 'athlete.html',{'athlete': athlete, 'images': images})    

def blog(request):
    page = Page.objects.get(page='blog')
    posts = Post.objects.filter(published = 'True')
    posts = posts.order_by('postDate')
    return render(request, 'blog.html',{'page': page, 'posts': posts})

def single_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'single-post.html', {'post': post})

def about(request):
    page = Page.objects.get(page='about')
    careerStages = CareerStage.objects.annotate(year_int=Cast('year', IntegerField())).order_by('-year_int')
    images = MyImage.objects.all()
    return render(request, 'about.html', {'page': page, 'careerStages': careerStages, 'images': images})

def impressum(request):
    page = Page.objects.get(page='impressum')
    return render(request, 'impressum.html', {'page': page})

def legal(request):
    page = Page.objects.get(page='legal')
    return render(request, 'legal.html', {'page': page})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def page_not_found(request,):
    return render(request, '404.html')