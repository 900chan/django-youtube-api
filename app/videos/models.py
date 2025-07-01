from django.db import models
from common.models import CommonModel
from users.models import User


class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField(blank=True) # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # upload_to='저장경로'

    # User : Video -> 1:N
    user = models.ForeignKey(User, on_delete=models.CASCADE)
