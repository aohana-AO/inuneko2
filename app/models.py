
from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from distutils.command.upload import upload
from tokenize import blank_re
from venv import create
# Create your models here.

class Health(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    problemCategory = models.TextField("カテゴリー")
    peopleNum = models.IntegerField("カロリー計算")
    created = models.DateTimeField("作成日", default=timezone.now)