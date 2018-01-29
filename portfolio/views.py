from django.views.generic import TemplateView
from .models import About, Contact, Domain, Experience, ExperienceType, Project, Publication, PublicationType

def get_ex(ex_type):
    rows = Experience.objects.filter(ex_type__title=ex_type)\
        .extra({'s': "DATE_FORMAT(start, '%%b. %%Y')", 'e': "DATE_FORMAT(end, '%%b. %%Y')"})\
        .values('s', 'e', 'title_kor', 'title_eng', 'location_kor', 'location_eng', 'desc_kor', 'desc_eng')\
        .order_by('-s')
    for entry in rows:
        if entry['e'] is None:
            entry['range_ko'] = "%s - 현재" % entry['s']
            entry['range_en'] = "%s - CURRENT" % entry['s']
        else:
            entry['range_ko'] = "%s - %s" % (entry['s'], entry['e'])
            entry['range_en'] = "%s - %s" % (entry['s'], entry['e'])
    return rows

class Index(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        # desc. text of myself
        context['about'] = About.objects.first()

        # contact info
        context['contacts'] = Contact.objects.all()

        # domain
        context['domains'] = Domain.objects.all()

        # work experience
        context['works'] = get_ex("work")

        # educations
        context['edus'] = get_ex("edu")

        # projects
        '''context['projects'] = get_project()

        # papers
        context['papers'] = get_publication("paper")

        # reports
        context['reports'] = get_publication("report")

        # awards
        context['awards'] = get_award()'''

        return context
