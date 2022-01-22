from django.db import models


class Tasks(models.Model):
    title=models.CharField(max_length=200,null=True,blank=False)
    status=models.BooleanField(null=True,blank=False,default=False)
    
    def __str__(self):
        return self.title
