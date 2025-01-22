from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Zone, Feedback
from .serializers import ZoneSerializer, FeedbackSerializer

from django.shortcuts import get_object_or_404  # Import added
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def update_feedback(request, feedback_id):
    if request.method == "PUT":
        feedback = get_object_or_404(Feedback, feedback_id=feedback_id)
        data = json.loads(request.body)
        feedback.user_email = data.get("user_email", feedback.user_email)
        feedback.zone_name = data.get("zone_name", feedback.zone_name)
        feedback.feedback_text = data.get("feedback_text", feedback.feedback_text)
        feedback.user_coordinates = data.get("user_coordinates", feedback.user_coordinates)
        feedback.save()
        return JsonResponse({"message": "Feedback updated successfully!"}, status=200)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)


# View to fetch zones data
@api_view(['GET'])
def get_zones(request):
    zones = Zone.objects.all()  # Fetch all zones
    serializer = ZoneSerializer(zones, many=True)
    return Response(serializer.data)

# View to submit feedback
@api_view(['POST'])
def submit_feedback(request):
    # Deserialize the feedback data
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the feedback to the database
        return Response({"message": "Feedback submitted successfully!"}, status=201)
    else:
        return Response(serializer.errors, status=400)

