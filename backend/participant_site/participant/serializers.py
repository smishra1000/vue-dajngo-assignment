from rest_framework import serializers
from . import models


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'foundation_date', 'participant_type','ranking',)
        model = models.Participant