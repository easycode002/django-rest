# test_app/serializers.py
from rest_framework import serializers

class DataSourceSerializer(serializers.Serializer):
    source_name = serializers.CharField(max_length=100)
    source_type = serializers.CharField(max_length=50)
    source_format = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    source_path = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)

    # Define additional fields as needed
    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return validated_data
