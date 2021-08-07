from rest_framework import serializers

class StudentDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    number = serializers.IntegerField()
