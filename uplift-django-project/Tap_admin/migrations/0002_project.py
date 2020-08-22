# Generated by Django 3.0.1 on 2019-12-27 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(max_length=20)),
                ('project_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('sqfeet', models.DecimalField(decimal_places=5, max_digits=10)),
                ('proj_sale_status', models.CharField(choices=[('Completed', 'Completed'), ('in_process', 'in-process'), ('not_started', 'Not started')], default='not_started', max_length=15)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
