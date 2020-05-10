# Generated by Django 3.0.5 on 2020-04-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200421_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %r is not a valid choice.', 'null': 'This field cannot be null.'}, max_length=10),
        ),
    ]
