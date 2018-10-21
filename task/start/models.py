from django.db import models

STATUS_CHOICES = (
    (1, 'PHONE'),
    (2, 'FACEBOOK'),
    (3, 'EMAIL'),
)


class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    category = models.CharField(max_length=100, verbose_name='Категория')
    logo = models.CharField(max_length=100, verbose_name='Логотип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Branch(models.Model):
    address = models.CharField(max_length=100, verbose_name='Адрес')
    latitude = models.CharField(max_length=100, verbose_name='Широта')
    longitude = models.CharField(max_length=100, verbose_name='Долгота')
    courses = models.ForeignKey(Courses, related_name='branches', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.address


class Contact(models.Model):
    type = models.IntegerField(choices=STATUS_CHOICES, default=1)
    value = models.CharField(max_length=100)
    courses = models.ForeignKey(Courses, related_name='contacts', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.type
