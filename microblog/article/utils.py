from django.core.exceptions import ValidationError


def validate_title(value):
    from django.conf import settings

    if value.lower() in settings.PROHIBITED_NAMES:
        raise ValidationError('nazwa %s jest zakazana' % value.capitalize())
