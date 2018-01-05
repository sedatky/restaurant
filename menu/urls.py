from django.conf.urls import url
from .import views

urlpatterns = [
   url(r'^$',views.index,name='index'),  #defAULT HOMEPAGE
  #  url(r"^(?P<id>[0-9]+)/$", views.types, name='details'),
    url(r'^types/',views.types,name='types'),
    url(r'^food_types/',views.food_type,name='food_types'),
    url(r'^foods/',views.food,name='foods'),
]