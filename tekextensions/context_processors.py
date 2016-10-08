from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


# noinspection PyUnusedLocal
def static_url_prefix(request):
    return {'STATIC_URL': settings.STATIC_URL}


def current_site(request):
    """
    A context processor to add the "current_site" to the current Context

    """

    context_name = 'CURRENT_SITE'
    site = get_current_site
    return {context_name: site}
