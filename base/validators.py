"""Validators"""

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FileSizeValidator:
    message = _(
        'The maximum file size that can be uploaded is %(size)s MB.'
    )
    code = 'invalid_size'

    def __init__(self, size=None, message=None, code=None):
        if size is None:
            size = 25
        self.size = size * 1048576
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if value.size > self.size:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    'size': self.size / 1048576,
                }
            )

    def __eq__(self, other):
        return (
                isinstance(other, self.__class__) and
                self.size == other.size and
                self.message == other.message and
                self.code == other.code
        )
