from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __srt__(self):
        return'{}'.format(self.descripcion)
    
        def save(self):
            self.descripcion = self.descripcion.upper() 
            super(Categoria, self).save()

    class Meta:
        verbose_name_plural="Categorias"