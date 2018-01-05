# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Types,Food_types,Foods
from django.shortcuts import render

# Create your views here.
def index(request):
    all_menu_types=Types.objects.all()
    context = {'all_menu_types': all_menu_types}
    return render(request, 'menu/types.html', context)





def types(request):
    all_menu_type = Types.objects.all()
    context = {'all_menu_types': all_menu_type}
    return render(request, 'menu/types.html', context)



def food_type(request):
    all_food_type=Food_types.objects.all()
    context = {'all_food_types': all_food_type}
    return render(request, 'menu/food_type.html', context)

def food(request):
    all_food = Foods.objects.all()
    context = {'all_food': all_food}
    return render(request, 'menu/food.html', context)

