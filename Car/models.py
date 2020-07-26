from django.db import models
from django.urls import reverse


class Car(models.Model):
    model = models.CharField(max_length=125, verbose_name='Модель авто')
    slug = models.SlugField(max_length=125, verbose_name='Url', unique=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, related_name='mans',
                                     verbose_name='Производитель')
    year_of_issue = models.IntegerField(verbose_name='Год выпуска')
    content = models.TextField(blank=True, verbose_name='Описание')

    MECHANIC = 1
    AUTOMATIC = 2
    ROBOT = 3

    GEAR_BOX_CHOICES = [
        (MECHANIC, 'Механика'),
        (AUTOMATIC, 'Автомат'),
        (ROBOT, 'Робот')
    ]

    gear_box = models.SmallIntegerField(default=MECHANIC, choices=GEAR_BOX_CHOICES, verbose_name='Коробка передач')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_banner = models.BooleanField(default=False)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('car', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['manufacturer']


class Manufacturer(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('manufacturer', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
