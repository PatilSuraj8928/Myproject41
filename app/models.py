from django.db import models

# Create your models here.
class BheemaGF(models.Model):
    instaId=models.IntegerField(primary_key=True)
    gfname=models.CharField(max_length=100)
    mobile=models.IntegerField()

    def __str__(self):
        return self.name