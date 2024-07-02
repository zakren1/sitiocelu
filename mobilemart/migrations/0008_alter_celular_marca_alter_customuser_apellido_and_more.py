# Generated by Django 5.0.6 on 2024-07-02 23:19

import django.core.validators
import mobilemart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilemart', '0007_alter_celular_marca_pedido_detallepedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celular',
            name='marca',
            field=models.CharField(choices=[('Xiaomi', 'Xiaomi'), ('Samsung', 'Samsung'), ('Apple', 'Apple')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='apellido',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='El apellido debe tener al menos 3 caracteres')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='El nombre debe tener al menos 3 caracteres')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rut',
            field=models.CharField(max_length=12, validators=[mobilemart.models.validar_rut]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefono',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{9}$', 'El teléfono debe contener exactamente 9 números.')], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, message='El nombre de usuario debe tener al menos 3 caracteres')], verbose_name='Nombre de usuario'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=20),
        ),
    ]