from rest_framework import serializers

from music.models import Song, Podcast, Audiobook


class AddSerializer(serializers.ModelSerializer):
    """docstring for AddSerializer"""

    class Meta:
        """docstring for meta"""
        model = Song
        fields = "__all__"


class AddSerializerPodcast(serializers.ModelSerializer):
    """docstring for AddSerializer"""

    class Meta:
        """docstring for meta"""
        model = Podcast
        fields = "__all__"


class AddSerializerAudiobook(serializers.ModelSerializer):
    """docstring for AddSerializer"""

    class Meta:
        """docstring for meta"""
        model = Audiobook
        fields = "__all__"
