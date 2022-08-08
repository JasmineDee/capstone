from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User,related_name='entries',on_delete=models.CASCADE, null=True ,blank=True)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'