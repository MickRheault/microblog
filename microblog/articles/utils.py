from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_title(value):
    from django.conf import settings

    if value.lower() in settings.PROHIBITED_NAMES:
        raise ValidationError(
            _('%s name is prohibited' % value.capitalize()))