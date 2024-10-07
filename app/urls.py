from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('properties', views.properties, name='properties'),
    path('property_info/<str:slug>', views.property_info, name='property_info'),
    path('projects', views.projects, name='projects'),
    path('project_info/<str:slug>', views.project_info, name='project_info'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog_info/<str:slug>', views.blog_info, name='blog_info'),
]