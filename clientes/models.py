from django.db import models


class Cliente(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    name = models.CharField(
        max_length=75, null=False, blank=False, verbose_name='nome'
    )

    phone = models.CharField(
        max_length=11, null=False, blank=False, verbose_name='telefone'
    )

    city = models.CharField(
        max_length=75, null=False, blank=False, verbose_name='cidade'
    )

    states = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RR', 'Roraima'),
        ('RO', 'Rondônia'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

    state = models.CharField(
        choices=states, default='RO', max_length=2, null=False, blank=False, verbose_name='estado'
    )

    street = models.CharField(
        max_length=75, null=False, blank=False, verbose_name='rua'
    )

    number = models.CharField(
        max_length=75, null=False, blank=False, verbose_name='número'
    )

    district = models.CharField(
        max_length=75, null=False, blank=False, verbose_name='bairro'
    )

    complement = models.CharField(
        max_length=75, null=True, blank=True, verbose_name='complemento'
    )
    
    def __str__(self):
        return self.name
