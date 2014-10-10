from tastypie.resources import ModelResource
from members.models import Member

class MemberResource(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        allowed_methods = ['get']