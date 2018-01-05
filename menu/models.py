# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Types(models.Model):
    menu_type=models.CharField(max_length=250)
    def __str__(self):
        return self.menu_type
class Food_types(models.Model):
    type=models.ForeignKey(Types,on_delete=models.CASCADE)
    food_type=models.CharField(max_length=250)

    def __str__(self):
        return self.food_type
class Foods(models.Model):
    food_types=models.ForeignKey(Food_types,on_delete=models.CASCADE)
    food=models.CharField(max_length=250)
    def __str__(self):
        return self.food