# Generated by Django 4.2.7 on 2023-12-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connecte', '0003_alter_produit_prix_alter_produit_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.SlugField(default='', max_length=120),
            preserve_default=False,
        ),
    ]