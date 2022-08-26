from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="projects")
    description = models.TextField()
    url = models.URLField(null=True, blank=True)

class Team(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="team")
    description = models.TextField()
    github_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)

class Reviews(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    review = models.TextField()
    designation = models.CharField(max_length=200)
