from tastypie.resources import ModelResource
from members.models import Member
from sorl.thumbnail import get_thumbnail

class MemberResource(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        bundle.data['thumb'] = get_thumbnail(bundle.obj.photo, '100x100', crop='center')
        return bundle