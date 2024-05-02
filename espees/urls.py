from django.urls import path
from .views import create_avatar, image_processing

urlpatterns = [
    path('', create_avatar, name='avatar' ),
    path('processing_image', image_processing, name="process" )
]
