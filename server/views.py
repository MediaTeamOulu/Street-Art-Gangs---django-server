from server.models import Team, User, Venue
from server.serializers import TeamSerializer, VenueSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TeamList(APIView):
    """
    List all the teams, or create a new team.
    """
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):
    """
    Retrieve, update or delete a team instance.
    """
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
