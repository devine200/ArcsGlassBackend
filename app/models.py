from django.db import models
from django.utils.text import slugify
from uuid import uuid4

class LandingPageCarousel(models.Model):
    cover_photo = models.ImageField(upload_to="landing")
    heading = models.CharField(max_length=200)
    description = models.TextField()
    redirect_text = models.CharField(max_length=20)
    redirect_link = models.CharField(max_length=250)
    
    def __str__(self):
        return self.heading
    

class LandingPageProjectsIntro(models.Model):
    description = models.TextField()
    cover_photo = models.ImageField(upload_to="landing")
    
    def __str__(self):
        return "Landing Page Intro Text"
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=20, null=True)
    property_type = models.CharField(max_length=20, null=True)
    style = models.CharField(max_length=50, null=True)
    year_of_execution = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_images")
    image = models.ImageField(upload_to="project")
    
    def __str__(self):
        return f"{self.project.name} Project Image \t\t[{self.image.name}]"

HOME_UNIT_CHOICES = [("COMMERCIAL", "commercial"), ("residential", "RESIDENTIAL")]
class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.FloatField()
    bedroom_count = models.PositiveIntegerField(default=0)
    bathroom_count = models.PositiveIntegerField(default=0)
    parking_space_count = models.PositiveIntegerField(default=0)
    home_unit_count = models.PositiveIntegerField(default=0)
    property_type = models.CharField(max_length=50, choices=HOME_UNIT_CHOICES, default="duplex")
    description = models.TextField(default="")
    slug = models.SlugField(unique=True, max_length=255, default=f"{str(uuid4())}")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class PropertyAmenity(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_amenities")
    amenity = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{property.name.capitalize()}'s Amenity: {self.amenity}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="property_images")
    image = models.ImageField(upload_to="property")
    
    def __str__(self):
        return f"{self.property.name} Property Image \t\t[{self.image.name}]"
        
        
class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255)
    client = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    scope = models.CharField(max_length=100)
    collaborator = models.CharField(max_length=100)
    description_top = models.TextField()
    description_bottom = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    
class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_images")
    image = models.ImageField(upload_to="blog")
    
    def __str__(self):
        return f"{self.blog.title} Blog Image [{self.image.name}]"
    
class SiteInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    about_us = models.TextField(default="")
    
    def __str__(self):
        return "ARC N GLASS website information"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Contacted By: {self.name} \n Time Stamp: {self.created_at}"
    

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="team_members", default="/media/profile.jpg")
    
    def __str__(self):
        return f"Team {self.position.capitalize()}: {self.name.capitalize()}"