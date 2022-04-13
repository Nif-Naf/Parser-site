from django.db import models

class External(models.Model):
    """Для использования передачи адреса."""
    url = models.CharField('Адрес', max_length=100)

class Result(models.Model):
    """Модель """
    url = models.CharField('Адрес', max_length=50)
    domains = models.CharField('Домен', max_length=30)
    create_data = models.DateTimeField('Дата создания', auto_now=True)
    update_data = models.DateTimeField('Дата обновления', auto_now_add=True)
    contry = models.CharField('Страна', max_length=20)
    is_dead = models.CharField('Хз что это', max_length=30)
    a = models.CharField('', max_length=30)
    ns = models.CharField('', max_length=30)
    cname = models.CharField('', max_length=30)
    mx = models.CharField('', max_length=30)
    txt = models.CharField('', max_length=30)


    def __str__(self):
        """Название."""
        return self.domains

    class Meta:
        """Для отображение в админке."""
        verbose_name = 'Данные парсинга'
        verbose_name_plural = 'Данные парсинга'