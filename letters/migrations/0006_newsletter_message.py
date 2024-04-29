# Generated by Django 4.2.5 on 2024-04-27 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0005_newsletter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='letters.message', verbose_name='Сообщение'),
        ),
    ]