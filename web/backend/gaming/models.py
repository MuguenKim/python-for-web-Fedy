from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Gamer(models.Model):
    userName = models.CharField(max_length=30, primary_key=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.userName
