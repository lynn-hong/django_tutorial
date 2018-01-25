from django.contrib import admin
from .models import About, Domain, Experience, ExperienceType, Project, Publication, PublicationType


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

@admin.register(ExperienceType)
class ExperienceTypeAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

@admin.register(PublicationType)
class PublicationTypeAdmin(admin.ModelAdmin):
    #list_display = ['about_me', 'home_img']
    #list_display_links = ['title']
    pass

