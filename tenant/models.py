from django.db import models

from datetime import date


# Create your models here.

class Tenant(models.Model):
    title = models.CharField(verbose_name='Título', max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateField(verbose_name='Atualizado em:',null=False, blank=False)


    class Meta:
        ordering = ["title"]


