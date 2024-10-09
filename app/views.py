from django.shortcuts import render, get_object_or_404
from app.models import (
    LandingPageCarousel,
    SiteInfo,
    Project,
    Property,
    Blog,
    TeamMember,
    LandingPageProjectsIntro,
    ContactMessage
)


def index(request):
    carousels = LandingPageCarousel.objects.all()
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    latest_projects = Project.objects.all().order_by("-created_at")[:5]
    intro_text = LandingPageProjectsIntro.objects.first()
    empty_slots_range = range(5 - len(latest_projects))
    return render(
        request,
        "index.html",
        {
            "carousels": carousels,
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "latest_projects": latest_projects,
            "empty_slots": empty_slots_range,
            "intro_text": intro_text,
        },
    )


def about(request):
    team_members = TeamMember.objects.all()
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "about.html",
        context={
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "team_members": team_members,
        },
    )


def blog(request):
    blogs = Blog.objects.all()
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "blog.html",
        context={
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "blogs": blogs,
        },
    )


def projects(request):
    site_info = SiteInfo.objects.first()
    projects = Project.objects.all()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]

    return render(
        request,
        "projects.html",
        context={
            "site_info": site_info,
            "projects": projects,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
        },
    )


def project_info(request, slug):
    site_info = SiteInfo.objects.first()
    project = get_object_or_404(Project, slug=slug)
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "project_info.html",
        context={
            "site_info": site_info,
            "project": project,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
        },
    )


def properties(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    properties = Property.objects.all()

    if request.method == "POST":
        property_type = request.POST.get("property_type", "")
        price = int(request.POST.get("price", 0))
        bedroom_count = int(request.POST.get("bedrooms", 0))
        bathroom_count = int(request.POST.get("bathrooms", 0))
        
        if property_type != "":
            properties = properties.filter(property_type=property_type)
            
        if price and int(price) > 0:
            print(price)
            properties = properties.filter(price__gte=int(price))
        
        if bedroom_count > 0 :
            properties = properties.filter(bedroom_count__lte=int(bedroom_count))

        if bathroom_count > 0:
            properties = properties.filter(bathroom_count__lte=int(bathroom_count))
        
    return render(
        request,
        "properties.html",
        context={
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "properties": properties,
        },
    )


def property_info(request, slug):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    property = get_object_or_404(Property, slug=slug)

    return render(
        request,
        "property_info.html",
        context={
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "property": property,
        },
    )


def contact(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    error_message = None
    success_message = None
    
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        message = request.POST.get("message", None)
        
        if name == None or email == None or phone == None or message == None:
            error_message = "Missing Field While Sending Message"
        
        else:
            try:
                ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
                success_message = "Contact Message Was Relayed Succesfully"
                
            except Exception as e:
                error_message = str(e)
            
    return render(
        request,
        "contact.html",
        context={
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "error_message": error_message,
            "success_message": success_message,
        },
    )


def blog_info(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    nav_latest_properties = Property.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "./blogs/blog_info.html",
        context={
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "nav_latest_properties": nav_latest_properties,
            "blog": blog,
        },
    )
