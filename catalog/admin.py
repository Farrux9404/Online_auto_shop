from django.contrib import admin
from .models import Logo, Car, Contract, Contractsub


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ['title']
    fields = ('title_uz', 'descriptions_uz', 'descriptions_ru', 'image',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update', 'order',)
    search_fields = ['title']
    fields = ('title_uz', 'title_ru', 'descriptions_uz', 'descriptions_ru', 'filed_km', 'year', 'price', 'logo', 'image',
              'color')


class ContractsubInline(admin.TabularInline):
    model = Contractsub
    fields = ['inital_payment', 'month', 'year',]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('create', 'update',)
    inlines = [ContractsubInline]
    fields = ('car',)