# Generated by Django 4.0 on 2021-12-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=75, verbose_name='nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='preço')),
            ],
        ),
    ]
