# Generated by Django 3.2.8 on 2022-01-22 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0005_alter_integrantes_service_area'),
        ('posts', '0003_alter_posts_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='integrantes.integrantes'),
        ),
    ]
