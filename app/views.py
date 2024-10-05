from django.shortcuts import render, get_object_or_404
from app.models import LandingPageCarousel, SiteInfo, Project


def index(request):
    carousels = LandingPageCarousel.objects.all()
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    latest_projects = Project.objects.all().order_by("-created_at")[:5]
    empty_slots_range = range(5 - len(latest_projects))
    return render(
        request,
        "index.html",
        {
            "carousels": carousels,
            "site_info": site_info,
            "nav_latest_projects": nav_latest_projects,
            "latest_projects": latest_projects,
            "empty_slots": empty_slots_range
        },
    )


def about(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "about.html",
        context={"site_info": site_info, "nav_latest_projects": nav_latest_projects},
    )


def blog(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "blog.html",
        context={"site_info": site_info, "nav_latest_projects": nav_latest_projects},
    )


def projects(request):
    site_info = SiteInfo.objects.first()
    projects = Project.objects.all()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "projects.html",
        context={
            "site_info": site_info,
            "projects": projects,
            "nav_latest_projects": nav_latest_projects,
        },
    )


def project_info(request, slug):
    site_info = SiteInfo.objects.first()
    project = get_object_or_404(Project, slug=slug)
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "project_info.html",
        context={
            "site_info": site_info,
            "project": project,
            "nav_latest_projects": nav_latest_projects,
        },
    )


def properties(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "properties.html",
        context={"site_info": site_info, "nav_latest_projects": nav_latest_projects},
    )


def property_info(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "property_info.html",
        context={"site_info": site_info, "nav_latest_projects": nav_latest_projects},
    )


def contact(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "contact.html",
        context={"site_info": site_info, "nav_latest_projects": nav_latest_projects},
    )


def blog_info(request):
    site_info = SiteInfo.objects.first()
    nav_latest_projects = Project.objects.all().order_by("-created_at")[:3]
    return render(
        request,
        "./blogs/blog_info.html",
        context={"site_info": site_info, "nav_latest_projects": nav_latest_projects},
    )
