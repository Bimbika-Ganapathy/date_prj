# from django.urls import path
# from .views import cdt  # Import your view function

# urlpatterns = [
#     path('', cdt, name='home'),  # This makes http://127.0.0.1:8000/ work
#     path('date/', cdt, name='current_datetime'),
# ]

from django.urls import path
from .views import dynamicdate  # Import views

urlpatterns = [
    path('dynamic/<str:s>/', dynamicdate, name='dynamic_date'),  # Handles /dynamic/some-text/
]