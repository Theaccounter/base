"""Base Model"""

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """Use this model to auto add The following fields to each model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=50)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='%(class)s_created_by'
    )
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='%(class)s_updated_by'
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
