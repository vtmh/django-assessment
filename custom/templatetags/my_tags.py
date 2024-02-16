from django import template
from custom.models import SiteSetting
import pytz
from django.utils import timezone

register = template.Library()

@register.filter
def sitesetting(request):
    sitesetting = SiteSetting.objects.all().order_by('-id')[0:1]
    return sitesetting 


@register.filter
def all_time_zone(request):
    zones = pytz.all_timezones
    return zones

@register.filter
def current_time_zone(request):
    current_timezone = timezone.get_current_timezone_name()
    return current_timezone