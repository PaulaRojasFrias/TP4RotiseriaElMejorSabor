# Generated by Django 4.1.2 on 2022-10-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_plato', models.CharField(max_length=11, unique=True)),
                ('nombre_plato', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('tipo_plato', models.CharField(choices=[('entrada', 'Entrada'), ('plato principal', 'Plato principal'), ('postre', 'Postre')], max_length=20)),
                ('precio', models.CharField(max_length=4)),
                ('vigente', models.BooleanField()),
                ('tipo_menu', models.CharField(choices=[('vegetariano', 'Vegetariano'), ('celiaco', 'Celiaco'), ('diabetico', 'Diabetico'), ('normal', 'Normal')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoPedido', models.CharField(max_length=11, unique=True)),
                ('fecha_pedido', models.DateField()),
                ('estado_pedido', models.CharField(choices=[('pendiente', 'Pendiente'), ('en camino', 'En camino'), ('cancelado', 'Cancelado'), ('entregado', 'Entregado'), ('devuelto', 'Devuelto')], max_length=15)),
                ('tipo_entrega', models.CharField(choices=[('domicilio', 'Domicilio'), ('local', 'Local')], max_length=9)),
                ('horaInicioEntrega', models.TimeField()),
                ('horaFinEntrega', models.TimeField()),
                ('cadete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.cadete')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('plato', models.ManyToManyField(to='pedido.plato')),
            ],
        ),
    ]
