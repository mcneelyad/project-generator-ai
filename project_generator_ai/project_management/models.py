from django.db import models

from .constants import Platform, ProjectStatus

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    platform = models.CharField(max_length=20, choices=Platform.choices())
    framework = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=ProjectStatus.choices(), default=ProjectStatus.ACTIVE.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectComponent(models.Model):
    """Represents individual components of the project (UI, UX, backend, frontend, database) that users approve or reject."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.project.name}"

class ProjectFeature(models.Model):
    """A model to store additional features requested by users during the review process."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.project.name}"

class ProjectReview(models.Model):
    """A model to store reviews of the project by users."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.name} - {self.rating}"