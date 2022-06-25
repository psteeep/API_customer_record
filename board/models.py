from django.db import models


class Direction(models.Model):
    direction_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    sort_num = models.IntegerField()


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    direction = models.ForeignKey("Direction", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    birth_date = models.DateTimeField("data of birth")
    work_exp = models.IntegerField()
    sort_num = models.IntegerField()

