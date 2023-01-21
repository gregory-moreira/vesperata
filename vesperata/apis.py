from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Events
from .serializers import EventsSerializer
from rest_framework.permissions import AllowAny


class ListEventsAPI(APIView):
    def get(self, request):
        eventos = Events.objects.all().order_by('nome')
        serializer = EventsSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)