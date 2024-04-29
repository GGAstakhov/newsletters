# Generated by Django 4.2.5 on 2024-04-27 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0006_newsletter_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='maillog',
            name='newsletter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='letters.newsletter', verbose_name='Рассылка'),
        ),
    ]