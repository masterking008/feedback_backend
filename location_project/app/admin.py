from django.contrib import admin
from .models import Zone, Feedback


# admin.site.register(Zone)
admin.site.register(Zone,)

# Register the Feedback model
admin.site.register(Feedback)
