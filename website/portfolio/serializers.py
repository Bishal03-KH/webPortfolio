from rest_framework import serializers
from .models import Blog,Project,ContactForm


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','description','blog_image','published_at','updated_at']
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','project_image','description','published_at','updated_at'] 
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id','name','email','subject','message','created_at']         
               