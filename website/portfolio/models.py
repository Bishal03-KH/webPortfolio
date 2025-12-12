from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

#About
class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    bio = CKEditor5Field('Text', config_name='extends')
    logo = models.ImageField(upload_to='logo/')
    profile_image = models.ImageField(upload_to='profiles/')
    email = models.EmailField()
    address = models.CharField(max_length=100,blank=True,null=True)
    description = CKEditor5Field('Text', config_name='extends',blank=True)
    
    def __str__(self):
        return self.name
    
#Skills    
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    # icon = models.CharField(max_length=50,null=True,blank=True) 
    # proficiency = models.IntegerField()
    
    def __str__(self):
        return self.skill_name
    
#Blog   
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description =  CKEditor5Field('Text', config_name='extends')  
    blog_image = models.ImageField(upload_to='blogs/',blank=True,null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
#Contact
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self. name} - {self.email}"
    
    
#Social Media  
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    
    def __str__(self):
        return self.platform
    
    
#Resume/CV
class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
#Project

class Project(models.Model):
    title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to='project/',blank=True,null=True)
    description =  CKEditor5Field('Text', config_name='extends')
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.title
    
    
#background image
class BackgroundImage(models.Model):
    background = models.ImageField(upload_to='backgrounds/')
    
        
    
    
         
    
    
     

    
    
        
    
        