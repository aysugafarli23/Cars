from django.contrib import admin
from .models import Owner, Car, Rentacar

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner', 'rentacar')

@admin.register(Rentacar)
class RentacarAdmin(admin.ModelAdmin):
    list_display = ('company_name',)