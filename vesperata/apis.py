from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny


class ListEventAPI(APIView):
    def get(self, request):
        eventos = Event.objects.all().order_by('date')
        serializer = EventSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)