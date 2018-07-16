from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='部门名称')

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='职位名称')

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name='组别')

    class Meta:
        verbose_name = '组别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    USER_TYPE_CHOICES = (
        (u'0', u'普通用户'),
        (u'1', u'一级用户'),
    )
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.real_name

class AreaInfo(models.Model):
    id = models.BigIntegerField(verbose_name='ID', primary_key=True)
    name = models.CharField(max_length=100, verbose_name='地区名称')
    parent_id = models.BigIntegerField(verbose_name='上级ID')

    class Meta:
        verbose_name = '省市县地区'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Content(models.Model):
    user = models.ForeignKey(User, verbose_name='负责人', on_delete=models.CASCADE)
    area_info = models.ForeignKey(AreaInfo, verbose_name='地区', on_delete=models.CASCADE)

    wechat_id = models.CharField(max_length=64,verbose_name='微信ID')

    original_fans_num = models.IntegerField(verbose_name='原始粉丝数量', default=0)
    active_fans_num = models.IntegerField(verbose_name='主动加粉数量', default=0)
    passive_fans_num = models.IntegerField(verbose_name='被动加粉数量', default=0)

    send_invited_num = models.IntegerField(verbose_name='发出的好友邀请数量', default=0)
    dialog_num = models.IntegerField(verbose_name='对话数量', default=0)
    send_zone_num = models.IntegerField(verbose_name='推送朋友圈数量', default=0)
    group_add_num = models.IntegerField(verbose_name='加群数量', default=0)
    send_zone_for_friend_num = models.IntegerField(verbose_name='帮忙推送朋友圈数量', default=0)

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = '加粉登记表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username


class Province(models.Model):
    province_id = models.IntegerField(verbose_name='省份id', unique=True)
    province_name = models.CharField(max_length=32, verbose_name='省份名称')

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.province_name


class City(models.Model):
    province_id = models.IntegerField(verbose_name='省份id')
    city_id = models.BigIntegerField(verbose_name='市id',unique=True)
    city_name = models.CharField(max_length=64, verbose_name='市名称')

    class Meta:
        verbose_name = '市份'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.city_name


class County(models.Model):
    city_id = models.BigIntegerField(verbose_name='市id')
    county_id = models.BigIntegerField(verbose_name='县id')
    county_name = models.CharField(max_length=64, verbose_name='县名称')

    class Meta:
        verbose_name = '区县'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.county_name

class WechatInfo(models.Model):
    wechatId = models.CharField(max_length=100, verbose_name='微信ID')
    QRCode = models.ImageField(upload_to='upload/', verbose_name='微信二维码')
    STATE_CHOICES = (
        (u'0', u'封号'),
        (u'1', u'正常'),
    )
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=1)


    class Meta:
        verbose_name = '微信账户'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.wechatId