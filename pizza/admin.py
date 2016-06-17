from django.contrib import admin

from pizza.models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
