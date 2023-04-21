from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MenuCategories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    parent = models.ForeignKey('self', default=None, on_delete=models.CASCADE, **NULLABLE,
                               verbose_name='Родительский пункт', related_name='child_item')
    url = models.URLField(verbose_name='url')
    link = models.CharField(max_length=200, default='/', verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
