from django.db import models

# Create your models here.

class BaseModel(models.Model):

    state = models.BooleanField('Estado', default=True)
    created_at = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo base'
        verbose_name_plural = 'Modelos base'