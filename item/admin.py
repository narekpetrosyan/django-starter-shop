from django.contrib import admin
from item.models import Category, Item

admin.site.register([Category, Item])
