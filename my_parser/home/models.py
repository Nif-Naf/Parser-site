from django.db import models

class External(models.Model):
    """Для использования передачи адреса."""
    url = models.CharField('Адрес', max_length=100)

class Result(models.Model):
    """Модель """
    url = models.CharField('Адрес', max_length=500)
    domains = models.CharField('Домен', max_length=300)
    create_data = models.CharField('Дата создания', max_length=200)
    update_data = models.CharField('Дата обновления', max_length=200)
    country = models.CharField('Страна', max_length=200)
    is_dead = models.CharField('Хз что это', max_length=300)
    a = models.CharField('', max_length=300)
    ns = models.CharField('', max_length=300)
    cname = models.CharField('', max_length=300)
    mx = models.CharField('', max_length=300)
    txt = models.CharField('', max_length=300)


    def __str__(self):
        """Название."""
        return self.domains

    class Meta:
        """Для отображение в админке."""
        verbose_name = 'Данные парсинга'
        verbose_name_plural = 'Данные парсинга'