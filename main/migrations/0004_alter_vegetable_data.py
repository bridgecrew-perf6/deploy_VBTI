# Generated by Django 4.0.2 on 2022-03-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_vegetable_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetable',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]