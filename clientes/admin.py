from django.contrib import admin

from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'street', 'number', 'district']


admin.site.register(Cliente, ClienteAdmin)
admin.site.disable_action('delete_selected')
