# Generated by Django 3.0.1 on 2020-02-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapadmin', '0005_delete_blog_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='enquiry_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
