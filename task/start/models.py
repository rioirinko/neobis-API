from django.db import models

STATUS_CHOICES = (
    (1, 'PHONE'),
    (2, 'FACEBOOK'),
    (3, 'EMAIL'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    imgpath = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE,
                                 verbose_name='Категория', null=True,)
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
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.address


class Contact(models.Model):
    type = models.IntegerField(choices=STATUS_CHOICES, default=1)
    value = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.type
