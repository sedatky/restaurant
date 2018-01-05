# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Types,Food_types,Foods
# Register your models here.
admin.site.register(Types)
admin.site.register(Food_types)
admin.site.register(Foods)