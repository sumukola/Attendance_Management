from django.db import models

# Create your models here.
class create_table(models.Model):
    rollno = models.IntegerField(primary_key=True,null=False,unique=True)
    usn = models.TextField(max_length=10,unique=True)
    name = models.TextField(max_length=20)
    
