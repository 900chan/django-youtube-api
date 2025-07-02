from rest_framework.serializers import ModelSerializer
from .models import Video

class VideoListSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
