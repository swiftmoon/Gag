# Generated by Django 3.2.7 on 2021-09-13 02:16

from django.db import migrations, models
import gag.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210911_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=gag.helpers.UploadTo('comment')),
        ),
    ]
