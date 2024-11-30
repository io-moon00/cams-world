from .models import Athlete, SocialMedia

def athletes(request):
    all_athletes = Athlete.objects.filter(published='True')
    return {'athletes': all_athletes}

def social_media(request):
    social_media = SocialMedia.objects.all()
    return {'social_media': social_media}