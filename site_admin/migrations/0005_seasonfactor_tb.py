# Generated by Django 5.0.2 on 2024-02-27 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0004_season_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seasonfactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Season_factorname', models.TextField(max_length=20)),
                ('Season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.season_tb')),
            ],
        ),
    ]
