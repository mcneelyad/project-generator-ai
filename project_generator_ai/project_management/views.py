from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from .models import Project, ProjectComponent, ProjectFeature, ProjectReview
from .constants import ProjectStatus, Platform, Framework


def index(request):
    projects = Project.objects.all()
    return render(request, "project_management/list.html", {"projects": projects})


def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        platform = request.POST.get("platform")
        framework = request.POST.get("framework")
        project = Project.objects.create(
            name=name, description=description, platform=platform.lower(), framework=framework.lower()
        )
        project.save()
        return redirect("project_management:index")

    return render(
        request,
        "project_management/create.html",
        {
            "platforms": ProjectStatus.choices(),
            "platform_choices": Platform.choices(),
            "framework_choices": Framework.choices(),
        },
    )
