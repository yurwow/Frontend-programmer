from django.db import models

class Navigation(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Название профессии')
    logo_field = models.ImageField(upload_to='media/', blank = False, verbose_name='Логотип')
    first_menu = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=25)
    second_menu = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=25)
    thierd_menu = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=25)
    fourth_menu = models.TextField(blank=False, verbose_name='Четвертый пункт меню',max_length=25)
    fifth_menu = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=25)
    author = models.TextField(blank=False, verbose_name='Автор', max_length=50)

class Main(models.Model):
    text = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='media/', blank=False, verbose_name='Фото')

class Demand(models.Model):
    content = models.TextField(blank=True, verbose_name='Таблицы')
    photo1 = models.ImageField(upload_to='media/', blank = False, verbose_name='Первый график сравнения')
    photo2 = models.ImageField(upload_to='media/', blank = False, verbose_name='Второй график сравнения')

class Geography(models.Model):
    content = models.TextField(blank=True, verbose_name='Таблицы')
    first_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для первого фото')
    photo1 = models.ImageField(upload_to='media/', blank=False, verbose_name='Первое фото')
    second_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для второго фото')
    photo2 = models.ImageField(upload_to='media/', blank=False, verbose_name='Второй график')

class Skills(models.Model):
    first_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для таблицы')
    content = models.TextField(blank=True, verbose_name='Таблица')
    graph = models.ImageField(upload_to='media/', blank=False, verbose_name='График')


class LastVacancyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
