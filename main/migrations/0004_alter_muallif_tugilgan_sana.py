# Generated by Django 5.2 on 2025-04-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_record_qaytarilgan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muallif',
            name='tugilgan_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
