from django.core.exceptions import ValidationError


# Custom validators

def validate_rate(value: int) -> int:
    """Validate rating customer comments."""
    if value > 5:
        raise ValidationError('امتیاز نمی تواند بیشتر از 5 باشد.')
    elif value <= 0:
        raise ValidationError('امتیاز نمی تواند صفر باشد.')
    else:
        return value


def validate_email(email: str) -> str:
    """Validate email address"""
    accepted_serivces = ['gmail.com', 'yahoo.com', 'protonmail.com', 'pm.me', 'hotmail.com', 'outlook.com']
    _, service = email.split('@')
    if service.lower() not in accepted_serivces:
        raise ValidationError('آدرس ایمیل از سرویس های ایمیل مشهور یا امن مانند گوگل، یاهو و... نمی باشد.')
    return email
