from django.db import models
from django.utils import timezone
# Create your models here.

# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

class BiAsrCount(models.Model):
    id = models.AutoField(primary_key=True)
    conv_id = models.CharField(max_length=255,blank=True, null=True)
    text_from = models.CharField(max_length=255,blank=True, null=True)
    asr_count = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bi_asrcount'