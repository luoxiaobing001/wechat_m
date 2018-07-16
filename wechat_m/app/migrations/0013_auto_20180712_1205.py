# Generated by Django 2.0.7 on 2018-07-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180712_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BigIntegerField(verbose_name='地区名称')),
                ('parent_id', models.BigIntegerField(verbose_name='上级ID')),
            ],
            options={
                'verbose_name': '省市县地区',
                'verbose_name_plural': '省市县地区',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='population',
            field=models.IntegerField(null=True, verbose_name='人口数量'),
        ),
    ]