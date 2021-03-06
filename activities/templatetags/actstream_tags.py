# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.template import loader, Context
from django.utils.translation import ugettext as _

from django.template import Library
register = Library()


@register.simple_tag
def actstream(obj, stream_type='user'):
    """
	Creates activity stream placeholder with DOM attributes allowing scripts
    to fetch proper content.
	"""
    ct = ContentType.objects.get_for_model(obj).pk
    template = loader.get_template('activities/actstream.html')
    context = Context({
        'ct': ct,
        'pk': obj.pk,
        'type': stream_type,
    })
    return template.render(context)
