from django.contrib import admin

# Register your models here.
from .models import Content, Province, City, County, Department, Position, User, AreaInfo,WechatInfo,Group

admin.site.site_header = '蓬勃快讯后台管理'
admin.site.site_title = '蓬勃快讯'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','real_name', 'department', 'position', 'user_type',)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'wechat_id', 'active_fans_num', 'passive_fans_num', 'create_time',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('province_id','city_id', 'city_name',)

class CountyAdmin(admin.ModelAdmin):
    list_display = ('city_id','county_id', 'county_name',)

class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ('name','parent_id',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'real_name', 'department', 'position', 'user_type',)

class WechatInfoAdmin(admin.ModelAdmin):
    list_display = ('wechatId', 'QRCode', 'state',)

admin.site.register(Position)
admin.site.register(Department)
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(WechatInfo, WechatInfoAdmin)
admin.site.register(Group)