from django.db import models

# - created_at: 데이터 생성시간
# - updated_at: 데이터 업데이트 시간
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True