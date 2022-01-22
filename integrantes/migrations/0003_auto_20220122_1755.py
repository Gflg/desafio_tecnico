# Generated by Django 3.2.8 on 2022-01-22 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
        ('integrantes', '0002_alter_integrantes_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='integrantes',
            name='area',
        ),
        migrations.AddField(
            model_name='integrantes',
            name='service_area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='servicos.servicos'),
        ),
    ]
