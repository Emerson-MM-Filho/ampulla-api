from django.db import models

class Produto(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    name = models.CharField(
        max_length=75, null=False, blank=False, verbose_name='nome'
    )

    price = models.DecimalField(
        max_digits=4, decimal_places=2, null=False, blank=False, verbose_name='preço'
    )

    def __str__(self):
        return self.name