# Generated by Django 3.0.4 on 2020-03-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0022_auto_20200324_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_sale_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('In Process', 'In Process'), ('Not Started', 'Not Started')], default='Not Started', max_length=15),
        ),
    ]
