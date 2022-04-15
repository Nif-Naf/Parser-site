from django.db import models

class External(models.Model):
    """Для использования передачи адреса."""
    url = models.CharField('Адрес', max_length=100)

class Result(models.Model):
    """Модель """
    url = models.CharField('Адрес', max_length=100)
    domains = models.CharField('Домен', max_length=300)
    create_data = models.DateTimeField('Дата создания')
    update_data = models.DateTimeField('Дата обновления')
    country = models.CharField('Страна', null=True, max_length=10)
    is_dead = models.CharField('Работает ли', null=True, max_length=300)
    a = models.CharField('Включена ли запись "А', null=True, max_length=300)
    ns = models.CharField('Включена ли запись "NS', null=True, max_length=300)
    cname = models.CharField('Включена ли запись "CNAME"', null=True, max_length=300)
    mx = models.CharField('Включена ли запись "MX"', null=True, max_length=300)
    txt = models.CharField('Включена ли запись "TXT"',null=True,  max_length=300)

    def __str__(self):
        """Название."""
        return ('URL: {} Domen: {}'.format(self.url, self.domains))

    class Meta:
        """Для отображение в админке."""
        verbose_name = 'Данные парсинга'
        verbose_name_plural = 'Данные парсинга'

class Messages(models.Model):
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    contacts = models.TextField(null=True, blank=True)
 
    def __str__(self):
        return self.title
