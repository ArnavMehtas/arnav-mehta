from django.db import models
from django_resized import ResizedImageField
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = ResizedImageField(
        size=[500,500],
        quality = 100 ,
        upload_to = 'profile_pics/',
        blank=True,
        null = True,
    )
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Python"
    category = models.CharField(max_length=50, choices=[
        ('language', 'Language'),
        ('framework', 'Framework'),
        ('tool', 'Tool'),
        ('design', 'Design'),
        ('database', 'Database'),
        ('other', 'Other'),
    ])

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    skills = models.ManyToManyField(Skill)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    date = models.DateField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.TextField()
    def __str__(self):
        return self.position
    
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year_completed = models.DateField()
    description = models.TextField()
    def __str__(self):
        return self.degree
    
class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.title