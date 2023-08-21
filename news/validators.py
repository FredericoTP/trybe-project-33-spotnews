from django.core.exceptions import ValidationError
from datetime import datetime


def validate_date_format(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")

        return True
    except ValueError:
        raise ValidationError(
            "Use o formato AAAA-MM-DD e uma data igual ou anterior a hoje."
        )


def validate_title(value):
    if not len(str(value).split()) > 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
