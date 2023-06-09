# Generated by Django 4.2 on 2023-05-31 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_chovatel_oceneni_zvire_delete_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='chovatel',
            name='cislo_prukazu',
            field=models.CharField(blank=True, error_messages={'blank': 'usí být vyplněno'}, help_text='Zadejte číslo průkazu', max_length=6, verbose_name='Prukaz'),
        ),
        migrations.AddField(
            model_name='zvire',
            name='cislo_zvirete',
            field=models.CharField(blank=True, error_messages={'blank': 'Musí být vyplněn'}, help_text='Zadejte cislo zvirete', max_length=100, verbose_name='Cislo zvirete'),
        ),
    ]
