# Generated by Django 4.0.4 on 2022-05-29 13:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ce08492d-b2a5-4254-9a61-5c17838437a3'), editable=False),
        ),
    ]