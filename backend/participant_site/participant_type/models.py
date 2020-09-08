# todos/models.py
from django.db import models


class ParticipantType(models.Model):
    id = models.IntegerField(primary_key=True)
    participant_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'master_participant_type'

    def __str__(self):
        """A string representation of the model."""
        return self.participant_type
