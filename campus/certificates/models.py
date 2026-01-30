from django.db import models
from participation.models import Participation
import uuid

class Certificate(models.Model):
    participation = models.OneToOneField(Participation, on_delete=models.CASCADE, related_name='certificate')
    certificate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return str(self.certificate_id)
