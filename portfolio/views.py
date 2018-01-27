from django.views.generic import TemplateView
from .models import About, Contact, Domain, Experience, ExperienceType, Project, Publication, PublicationType

class Index(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        # desc. text of myself
        context['about'] = About.objects.first()

        '''
        # contact info
        context['contacts'] = Contact.objects.all()

        # domain
        context['domains'] = get_domain()

        # work experience
        context['works'] = get_ex("work")

        # educations
        context['edus'] = get_ex("edu")

        # projects
        context['projects'] = get_project()

        # papers
        context['papers'] = get_publication("paper")

        # reports
        context['reports'] = get_publication("report")

        # awards
        context['awards'] = get_award()'''

        return context
