# Generated by Django 2.1 on 2018-12-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0003_auto_20180426_0048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readdetail',
            options={'verbose_name': '阅读详情', 'verbose_name_plural': '阅读详情'},
        ),
        migrations.AlterModelOptions(
            name='readnum',
            options={'verbose_name': '阅读数量', 'verbose_name_plural': '阅读数量'},
        ),
    ]
