from django.contrib import admin

from .models import *


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Produto, ProdutoAdmin)
