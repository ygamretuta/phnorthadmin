from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from members.models import Member
import sorl

@receiver(pre_delete, sender=Member)
def delete_thumbnail(sender, instance, **kwargs):
    sorl.thumbnail.delete(instance.photo)