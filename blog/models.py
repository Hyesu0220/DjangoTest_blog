from django.db import models
from django.utils import timezone

class Post(models.Model):
    # models.ForeignKey (외래키)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    # models.CharField - 글자 수가 제한된 텍스트를 정의
    title = models.CharField(max_length=200)
    # models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    text = models.TextField()
    # models.DateTimeField - 날짜와 시간을 의미
    created_data = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
