from django.db import models
from participant_type.models import ParticipantType
# Create your models here.
from django.db import models

class Participant(models.Model):
    email = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    foundation_date = models.DateTimeField(blank=True, null=True)
    participant_type = models.ForeignKey(ParticipantType, models.DO_NOTHING, db_column='participant_type')
    ranking = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participant'

    def __str__(self):
        return self.email