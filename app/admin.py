from django.contrib import admin

# Register your models here.
from .models import user, activity, duplicate


# Register your models here.
class duplicateadmin(admin.ModelAdmin):
    list_display = ['ok']


admin.site.register(duplicate)


class useradmin(admin.ModelAdmin):
    list_display = ['id', 'real_name', 'tz']


admin.site.register(user)


class activityadmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time']


admin.site.register(activity)