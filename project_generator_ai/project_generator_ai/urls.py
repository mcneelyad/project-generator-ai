from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(('project_management.urls', 'project_management'), namespace='project_management')),
]
