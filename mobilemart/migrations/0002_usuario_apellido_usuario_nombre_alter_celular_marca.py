# Generated by Django 5.0.6 on 2024-06-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilemart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='apellido', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='apellido', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='celular',
            name='marca',
            field=models.CharField(choices=[('XIAOMI', 'Xiaomi'), ('APPLE', 'Apple'), ('SAMSUNG', 'Samsung')], max_length=20),
        ),
    ]