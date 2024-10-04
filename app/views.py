from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def projects(request):
    return render(request, "projects.html")

def project_info(request):
    return render(request, "project_info.html")

def properties(request):
    return render(request, "properties.html")

def property_info(request):
    return render(request, "property_info.html")

def contact(request):
    return render(request, "contact.html")

def blog_info(request):
    return render(request, "./blogs/blog_info.html")
