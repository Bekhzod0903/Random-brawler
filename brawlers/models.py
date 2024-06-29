from django.db import models

# Create your models here.

class Category(models.Model):
    rarity = models.CharField(max_length=50)

    class Meta:
        db_table = ('category')

    def __str__(self):
        return f'{self.rarity}'

class Brawler(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table = ('brawler')

    def __str__(self):
        return f'{self.name}'