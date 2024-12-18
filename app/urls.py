from django.urls import path
from app import views, models

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("properties", views.properties, name="properties"),
    path("property_info/<str:slug>", views.property_info, name="property_info"),
    path("projects", views.projects, name="projects"),
    path("project_info/<str:slug>", views.project_info, name="project_info"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("blog_info/<str:slug>", views.blog_info, name="blog_info"),
    # path('project_upload', views.project_upload, name='project_upload'),
    # path('property_upload', views.property_upload, name='property_upload'),
]

if models.MultiUploadActivation.objects.first().is_active:
    urlpatterns += [
        path("project_upload", views.project_upload, name="project_upload"),
        path("property_upload", views.property_upload, name="property_upload"),
    ]
