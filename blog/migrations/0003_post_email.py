# Generated by Django 3.0.5 on 2020-04-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_boolean'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
