# Generated by Django 3.2.8 on 2022-01-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0004_alter_integrantes_service_area'),
        ('posts', '0002_alter_posts_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrantes.integrantes'),
        ),
    ]
