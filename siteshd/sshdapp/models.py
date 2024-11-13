from django.db import models

class Sezon(models.Model):

    name = models.CharField(max_length=20, unique=True)

    # Основные типы полей
    # дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логический
    # models.BooleanField
    # # Байты (blob)
    # models.BinaryField
    # # Картинка
    # models.ImageField
    # # Файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField

    def __str__(self):
        return self.name


class Razm(models.Model):

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Tovost(models.Model):

    uin = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    ostatok = models.DecimalField(max_digits=10, decimal_places=0)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kartss = models.TextField()
    ship = models.BooleanField()
    # Связь с сезонностью один - много
    sezonnost = models.ForeignKey(Sezon, on_delete=models.CASCADE)
    razmer = models.ForeignKey(Razm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
