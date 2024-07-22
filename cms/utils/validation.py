from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

def validate_image_format(image):
    valid_formats = ["JPEG", "PNG"]
    try:
        img = Image.open(image)
        if img.format not in valid_formats:
            raise ValidationError(
                _('Unsupported file format. Supported formats are: JPEG, PNG.'),
                code='invalid_format'
            )
    except Exception as e:
        raise ValidationError(
            _('Invalid image file.'),
            code='invalid_image'
        )

def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5MB
    if image.size > max_size:
        raise ValidationError(
            _('Image file too large. Maximum size allowed is 5MB.'),
            code='invalid_size'
        )
