from django.db import models


class Water(models.Model):
    location = models.CharField(
        max_length=150,
        verbose_name="Локация"
    )
    date = models.DateField(
        verbose_name="Дата доставки"
    )
    water_Liter = models.IntegerField(
        verbose_name="Сколько литров воды:"
    )
    quantity = models.IntegerField(
        verbose_name="Количество:"
    )
