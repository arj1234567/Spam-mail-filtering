# Generated by Django 5.0.2 on 2024-02-27 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_trash_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash_tb',
            name='Reciever_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_Id', to='user.register_tb'),
        ),
    ]