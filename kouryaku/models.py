from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    def __str__(self):
        return self.title
# models.py の修正例

class KouryakuPost(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=200)
    comment = models.TextField(verbose_name='コメント')
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='kouryakus',
        blank=True,
        null=True)
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)

    def __str__(self):
        return self.title

# 検索機能
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




