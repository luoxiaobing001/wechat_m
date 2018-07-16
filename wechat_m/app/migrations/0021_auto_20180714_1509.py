# Generated by Django 2.0.7 on 2018-07-14 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_content_wechat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='组别')),
            ],
            options={
                'verbose_name': '组别',
                'verbose_name_plural': '组别',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('0', '普通用户'), ('1', '一级用户')], max_length=2),
        ),
        migrations.AlterField(
            model_name='wechatinfo',
            name='state',
            field=models.CharField(choices=[('0', '封号'), ('1', '正常')], default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Group'),
        ),
    ]