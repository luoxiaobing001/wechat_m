# Generated by Django 2.0.7 on 2018-07-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180712_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '加粉登记表', 'verbose_name_plural': '加粉登记表'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '市份', 'verbose_name_plural': '市份'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name': '区县', 'verbose_name_plural': '区县'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '部门', 'verbose_name_plural': '部门'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': '职位', 'verbose_name_plural': '职位'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': '省份', 'verbose_name_plural': '省份'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='article',
            name='original_fans_num',
            field=models.IntegerField(default=0, verbose_name='原始粉丝数量'),
        ),
    ]
