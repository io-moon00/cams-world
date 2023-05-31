"""coachLamont URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import home, coaching, blog, athlets, athlet, about, impressum, legal, page_not_found
from forms import views

from django.urls import include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('coaching/', coaching, name='coaching'),
    path('athlets/', athlets, name='athlets'),
    path('athlet/<int:id>', athlet, name='athlet'),
    path('blog/', blog, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('impressum/', impressum, name='impressum'),
    path('legal/', legal, name='legal'),
    path('not/', page_not_found)
]

handler404 = "main.views.page_not_found_view"


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
