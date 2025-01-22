from django.urls import path
from . import views

urlpatterns = [
    path('api/zones/', views.get_zones, name='get_zones'),  # URL for fetching zones data
    path('api/submit-feedback/', views.submit_feedback, name='submit_feedback'),  # URL for submitting feedback
    path('api/submit-feedback/<int:feedback_id>/', views.update_feedback, name='update_feedback'),
]
