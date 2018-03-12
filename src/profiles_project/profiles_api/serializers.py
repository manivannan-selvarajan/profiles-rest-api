from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializers is a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)
