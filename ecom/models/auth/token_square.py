from django.db import models

from .token_base import TokenBaseModel


class SquareToken(TokenBaseModel):
    company_id = models.CharField(max_length=64)
