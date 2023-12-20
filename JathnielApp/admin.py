from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from JathnielApp.models import Videos, Comments

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)
admin.site.register(Comments)
