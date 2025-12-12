from .models import BackgroundImage,About,Skill, SocialLink

def background_image(request):
    bg_image = BackgroundImage.objects.first()
    return {'bg_image': bg_image}

def global_about(request):
    return {
        'about_detail':About.objects.first()
    }

def skill_and_social(request):
    skill_detail = Skill.objects.all()
    social_detail = SocialLink.objects.all()
    return {
        'skill_detail': skill_detail,
        'social_detail': social_detail
    }
