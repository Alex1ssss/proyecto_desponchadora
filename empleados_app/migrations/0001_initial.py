# Generated by Django 5.1 on 2024-12-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_empleado', models.CharField(max_length=20)),
                ('telefono_empleado', models.PositiveBigIntegerField()),
                ('correo_electronico', models.EmailField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('puesto_empleado', models.CharField(max_length=10)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
    ]
