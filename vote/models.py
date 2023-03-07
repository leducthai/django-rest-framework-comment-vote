from django.db import models

# Create your models here.

class vote(models.Model):
    user_id = models.IntegerField(null=False)
    pd_id = models.IntegerField(null=False)