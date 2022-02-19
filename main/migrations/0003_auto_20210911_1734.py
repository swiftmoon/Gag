# Generated by Django 3.2.7 on 2021-09-11 17:34

from django.db import migrations, models
import gag.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_postcomment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=gag.helpers.UploadTo('post'), verbose_name='Rasm/Video'),
        ),
    ]
