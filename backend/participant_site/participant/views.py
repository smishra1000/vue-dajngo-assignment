from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Participant
from .serializers import ParticipantSerializer


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from participant.models import Participant
from participant.serializers import ParticipantSerializer


@api_view(['GET', 'POST'])
def participant_list(request):
    """
    List all code participant, or create a new participant.
    """
    if request.method == 'GET':
        participant = Participant.objects.all()
        serializer = ParticipantSerializer(participant, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# , 'PUT', 'DELETE'
@api_view(['GET', 'POST']) 
def participant_detail(request, pk):
    """
    Retrieve, update or delete a code participant.
    """
    try:
        participant = Participant.objects.get(pk=pk)
    except Participant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParticipantSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)