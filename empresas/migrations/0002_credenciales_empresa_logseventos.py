# Generated by Django 5.1.4 on 2025-02-24 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credenciales_Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp_id', models.CharField(max_length=255, unique=True)),
                ('access_token', models.TextField()),
                ('token_expiracion', models.TextField()),
                ('webhook', models.TextField()),
                ('app_id', models.CharField(blank=True, max_length=255, null=True)),
                ('client_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_update', models.DateTimeField(auto_now_add=True)),
                ('business_id', models.CharField(max_length=255, unique=True)),
                ('Empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='LogsEventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField()),
                ('tipo_evento', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
            ],
        ),
    ]
