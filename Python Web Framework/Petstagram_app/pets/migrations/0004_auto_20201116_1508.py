# Generated by Django 3.1.2 on 2020-11-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20201029_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(upload_to='pets'),
        ),
    ]