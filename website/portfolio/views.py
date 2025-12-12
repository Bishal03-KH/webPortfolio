from django.shortcuts import render,get_object_or_404,redirect
from .models import About,Blog,ContactForm,Resume,Project
from django.contrib import messages
from rest_framework import viewsets
from .serializers import BlogSerializer,ProjectSerializer,ContactSerializer

# Create your views here.

def home(request):
    about_detail = About.objects.first()
    project_detail = Project.objects.all()
    
    return render(request, 'portfolio/home.html', {
        'about_detail': about_detail,
        'project_detail': project_detail,
        
    })
    
# def base(request):
#     skill_detail = Skill.objects.all()
#     social_detail = SocialLink.objects.all()
    
#     return render(request,'portfolio/base.html',{
#         'skill_detail': skill_detail,
#         'social_detail':social_detail,
        
#     })
        




def eachProjectDetail(request,id):
    each_detail = get_object_or_404(Project,id=id)
    
    return render(request,'portfolio/project_detail.html',{'each_detail':each_detail})




def eachBlogDetail(request):
    each_blog = Blog.objects.all()
    
    return render(request,'portfolio/blog_detail.html',{'each_blog':each_blog})




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        ContactForm.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        
        return redirect('home')

    return render(request,'portfolio/home.html')



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer   
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer        



