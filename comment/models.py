from django.db import models

# Create your models here.
class comment(models.Model):
    user_id = models.IntegerField(null=False)
    pd_id = models.IntegerField(null=False)
    body = models.TextField(null=False)

    @property
    def comment(self):
        return self.body

