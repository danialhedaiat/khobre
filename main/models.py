import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    joinDate = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Books(models.Model):
    pegiChoice = (("Babies", "Babies"),
                  ("Kids", "Kids"),
                  ("Young Teenagers", "Young Teenagers"),
                  ("Teenagers", "Teenagers"),
                  ("Adults", "Adults"))
    name = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    Pegi = models.CharField(choices=pegiChoice, max_length=20)
    auther = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, related_name="book")
    rented = models.BooleanField(default=False)
    archiveDate = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


class Barrow(models.Model):
    user = models.ForeignKey(User, related_name="barrow", on_delete=models.CASCADE)
    book = models.ForeignKey(Books, related_name="barrow", on_delete=models.CASCADE)
    borrowDate = models.DateTimeField(default=datetime.datetime.now())
    returnDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username + " " + self.book.name + " " + self.borrowDate.strftime("yyyy/mm/dd")

