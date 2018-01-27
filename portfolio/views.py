from django.views.generic import TemplateView
from .models import About, Contact, Domain, Experience, ExperienceType, Project, Publication, PublicationType

class Index(TemplateView):
    template_name = 'portfolio/index.html'