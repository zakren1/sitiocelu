# Generated by Django 5.0.6 on 2024-06-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilemart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celular',
            name='marca',
            field=models.CharField(choices=[('Xiaomi', 'Xiaomi'), ('Apple', 'Apple'), ('Samsung', 'Samsung')], max_length=20),
        ),
    ]
