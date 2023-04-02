# Generated by Django 4.1.7 on 2023-03-30 12:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_amenities_uid_alter_hotel_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4e44705e-309a-4468-ac9a-b357210eb9e1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4e44705e-309a-4468-ac9a-b357210eb9e1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4e44705e-309a-4468-ac9a-b357210eb9e1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hotelimages',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4e44705e-309a-4468-ac9a-b357210eb9e1'), primary_key=True, serialize=False),
        ),
    ]