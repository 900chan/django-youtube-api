from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Video
from users.serializers import UserInfoSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction


class VideoListSerializer(ModelSerializer):

    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

# 댓글 정보 추가
class VideoDetailSerializer(ModelSerializer):
    user = UserInfoSerializer(read_only=True)

    # Video:Comment (FK-자녀)
    # - Reverse Accessor = 부모가 자녀를 찾을 때 활용
    comment_set = CommentSerializer(many=True, read_only=True)

    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'

    def get_reactions(self, video):
        return Reaction.get_video_reactions(video)