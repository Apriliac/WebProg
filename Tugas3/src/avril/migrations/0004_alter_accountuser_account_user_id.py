# Generated by Django 5.0.4 on 2024-06-26 05:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avril', '0003_alter_accountuser_account_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.UUID('866e789e-57fe-44cc-8ff2-dbdfb9dcda3e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
