# models.py

from django.db import models

class Zone(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default='user')  # Name is required
    coordinates = models.JSONField(blank=True, null=True)  # Coordinates are optional

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user_email = models.EmailField(blank=False, null=False, default='test@example.com')  # Provide a default value here
    feedback_id = models.CharField(max_length=255, unique=True, blank=False, null=False)  # Feedback ID is required
    zone_name = models.CharField(max_length=255, blank=True, null=True)  # Zone can be null or blank
    feedback_text = models.TextField(blank=True, null=True)  # Feedback text is optional
    user_coordinates = models.JSONField(blank=True, null=True)  # Coordinates are optional

    def __str__(self):
        return f"Feedback from {self.user_email} in {self.zone_name}"
