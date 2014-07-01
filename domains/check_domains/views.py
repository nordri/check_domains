from check_domains.models import Domain
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def daysRemaining(d0, d1):
  return d0 - d1

def view_domain(request, days_left=0):
  domainList = []
  domains = Domain.objects.all().order_by('days')
  for domain in domains:
    daysLeft = daysRemaining (domain.days, datetime.today().date())
    d = (domain.name, daysLeft.days)
    domainList.append(d)
    
  return render_to_response('domains/view_domains.html',{ 'domainList':domainList, 'days_left':days_left }, context_instance=RequestContext(request))
