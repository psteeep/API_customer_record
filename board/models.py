from django.db import models
from django.urls import reverse


class Direction(models.Model):
    direction_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    sort_num = models.IntegerField()

    def __str__(self):
        return self.direction_name


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    direction = models.ManyToManyField(Direction)
    description = models.CharField(max_length=100)
    birth_date = models.DateTimeField("data of birth")
    work_exp = models.IntegerField()
    sort_num = models.IntegerField()

    def __str__(self):
        return self.doctor_name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

