from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Education , Achievement

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('skills',)  # Makes it easier to select multiple skills
    list_display = ('title', 'date', 'featured')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Achievement)
