# Generated by Django 4.2.5 on 2024-04-26 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maillog',
            options={'verbose_name': 'Лог', 'verbose_name_plural': 'Логи'},
        ),
    ]