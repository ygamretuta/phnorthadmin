from members.models import Member
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail
from util import admin

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumb')

    def thumb(self, obj):
        if obj.photo:
            t = get_thumbnail(obj.photo, '100x100', crop='center', quality=99)
            return u'<img src="%s"/>' % t.url
        else:
            return u'None'

    thumb.allow_tags = True

admin.site.register(Member, MemberAdmin)