from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'AP', 'エントリー'
        WEBEXAM = 'WE', 'Webテスト'
        WAITING = 'WT', 'メール待ち'
        INTERVIEW = 'IN', '面接'
        
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
        )
    title = models.CharField(max_length=100)
    status = models.CharField(
        max_length = 2,
        choices = Status.choices,
        default = Status.APPLIED
    )
    deadline = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
