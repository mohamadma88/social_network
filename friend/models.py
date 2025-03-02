from django.db import models
from account.models import User


class Friend(models.Model):
    req_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_to')
    req_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_from')
    is_accept = models.BooleanField(default=True)

    class Meta:
        unique_together = ['req_to', 'req_from']
