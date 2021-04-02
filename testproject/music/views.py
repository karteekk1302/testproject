from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from music.models import Song, Podcast, Audiobook
from music.serializer import AddSerializer, AddSerializerPodcast, AddSerializerAudiobook


class AddRecord(APIView):
    """docstring for AddRecord"""
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        """docstring"""
        try:
            type = int(request.POST.get('audioFileType', None))
            if type:
                if type == 1:
                    serializer = AddSerializer(data=request.data)
                if type == 2:
                    serializer = AddSerializer(data=request.data)
                if type == 3:
                    serializer = AddSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                data = serializer.validated_data
                data = serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                data = {"message": "audioFileType required."}
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(data, status=status_code)
        except Exception as e:
            data = {"message": "Server error."}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data, status=status_code)


class deleterecord(APIView):
    """docstring for AddRecord"""
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)

    def delete(self, request, *args, **kwargs):
        """delete location"""
        try:
            params = kwargs
            type = int(params.get('type', None))
            song_id = int(params.get('song_id', None))
            if type and song_id:
                if type == 1:
                    Song.objects.filter(id=song_id).delete()
                elif type == 2:
                    Podcast.objects.filter(id=song_id).delete()
                elif type == 3:
                    Audiobook.objects.filter(id=song_id).delete()

                return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            data = {"message": "Server error."}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data, status=status_code)

    def put(self, request, *args, **kwargs):
        """delete location"""
        try:
            params = kwargs
            type = int(params.get('type', None))
            song_id = int(params.get('song_id', None))
            if type and song_id:
                if type == 1:
                    instance = Song.objects.get(id=song_id)
                    serializer = AddSerializer(
                        instance,
                        data=request.data,
                        partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    data = serializer.save()

                elif type == 2:
                    instance = Podcast.objects.get(id=song_id)
                    serializer = AddSerializer(
                        instance,
                        data=request.data,
                        partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    data = serializer.save()
                elif type == 3:
                    instance = Audiobook.objects.get(id=song_id)
                    serializer = AddSerializer(
                        instance,
                        data=request.data,
                        partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    data = serializer.save()

                return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            data = {"message": "Server error."}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data, status=status_code)

    def get(self, request, *args, **kwargs):
        """delete location"""
        try:
            params = kwargs
            type = int(params.get('type', None))
            song_id = int(params.get('song_id', None))
            if type and song_id:
                if type == 1:
                    instances = Song.objects.filter(id=song_id)
                    serializer = AddSerializer(instances, many=True)
                elif type == 2:
                    instances = Podcast.objects.filter(id=song_id)
                    serializer = AddSerializer(instances, many=True)
                elif type == 3:
                    instances = Audiobook.objects.filter(id=song_id)
                    serializer = AddSerializer(instances, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            data = {"message": "Server error."}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data, status=status_code)
