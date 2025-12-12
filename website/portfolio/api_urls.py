from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, ProjectViewSet,ContactViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contacts', ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
