# Generated by Django 3.0.6 on 2020-05-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='media/images/already.png', upload_to='media/images/'),
        ),
    ]
