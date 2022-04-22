from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    """Модель данных для товара"""
    title = models.CharField('Наименование', max_length=100)
    price = models.FloatField('Цена', default=1, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
