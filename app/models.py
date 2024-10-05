from django.db import models
from django.utils.text import slugify

class LandingPageCarousel(models.Model):
    cover_photo = models.ImageField(upload_to="media/landing")
    heading = models.CharField(max_length=200)
    description = models.TextField()
    redirect_text = models.CharField(max_length=20)
    redirect_link = models.CharField(max_length=250)
    
    def __str__(self):
        return self.heading
    

class LandingPageProjectsIntro(models.Model):
    description = models.TextField()
    cover_photo = models.ImageField(upload_to="media/landing")
    

class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_images")
    image = models.ImageField(upload_to="project")
    
    def __str__(self):
        return f"{self.project.name} Project Image \t\t[{self.image.name}]"

class Property(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.FloatField()
    bedroom_count = models.PositiveIntegerField()
    bathroom_count = models.PositiveIntegerField()
    parking_space_count = models.PositiveIntegerField()
    home_unit_count = models.PositiveIntegerField()
    listing_count = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    

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
    image = models.ImageField(upload_to="media/blog")
    

class SiteInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Contacted By: {self.name} \n Time Stamp: {self.created_at}"
    