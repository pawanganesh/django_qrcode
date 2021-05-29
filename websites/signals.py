from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Website


@receiver(post_delete, sender=Website)
def post_delete_remove_file(sender, instance, *args, **kwargs):
    instance.qr_code.delete(False)
