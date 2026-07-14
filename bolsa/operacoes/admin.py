from django.contrib import admin
from .models import Operacao

# Register your models here.

#admin.site.register(Operacao)

@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = (
        "ticker",
        "tipo",
        "quantidade",
        "preco",
        "data_operacao",
    )