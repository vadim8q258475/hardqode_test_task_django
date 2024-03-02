from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    max_students_in_group = models.IntegerField()
    min_students_in_group = models.IntegerField()
    price = models.IntegerField(default=5000)

    def __str__(self):
        return f'{self.product_name}'


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return f'{self.lesson_name}'


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)
    group_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.group_name}'







