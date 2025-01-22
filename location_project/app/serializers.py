from rest_framework import serializers
from .models import Zone, Feedback

# Serializer for the Zone model
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'name', 'coordinates']  # Include necessary fields

# Serializer for the Feedback model

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user_email', 'feedback_id', 'zone_name', 'feedback_text', 'user_coordinates']
