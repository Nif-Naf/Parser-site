from django.db import models

class External(models.Model):
    """Для передачи адреса парсеру."""
    url = models.CharField('Адрес', max_length=100)

class Search(models.Model):
    """Для формы поиска."""
    search_object = models.CharField('Поиск запрошенного в БД:', max_length=100)

class Result(models.Model):
    """Модель """
    url = models.CharField('Адрес', max_length=100)
    domain = models.CharField('Домен', max_length=100)
    create_data = models.DateTimeField('Дата создания')
    update_data = models.DateTimeField('Дата обновления')
    country = models.CharField('Страна', null=True, max_length=10)
    is_dead = models.BooleanField('Работает ли')
    a = models.CharField('Включена ли запись "А', null=True, max_length=150)
    ns = models.CharField('Включена ли запись "NS', null=True, max_length=150)
    cname = models.CharField('Включена ли запись "CNAME"', null=True, max_length=150)
    mx = models.CharField('Включена ли запись "MX"', null=True, max_length=150)
    txt = models.CharField('Включена ли запись "TXT"',null=True,  max_length=150)

    def __str__(self):
        """Название."""
        return ('URL: {} Domen: {}'.format(self.url, self.domain))

    class Meta:
        """Для отображение в админке."""
        verbose_name = 'Данные парсинга'
        verbose_name_plural = 'Данные парсинга'