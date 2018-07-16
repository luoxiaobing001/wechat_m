# Generated by Django 2.0.7 on 2018-07-11 22:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180711_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('real_name', models.CharField(max_length=20, verbose_name='真实姓名')),
                ('user_type', models.CharField(choices=[(0, '普通用户'), (1, '一级用户')], max_length=2)),
            ],
            options={
                'verbose_name': '用户',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '加粉登记表'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '市份'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name': '区县'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '部门'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': '职位'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': '省份'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='article',
            name='fans_num',
        ),
        migrations.AddField(
            model_name='article',
            name='active_fans_num',
            field=models.IntegerField(default=0, verbose_name='主动加粉数量'),
        ),
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='passive_fans_num',
            field=models.IntegerField(default=0, verbose_name='被动加粉数量'),
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Position'),
        ),
    ]