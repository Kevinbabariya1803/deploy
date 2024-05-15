from django.db import models
import datetime
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class account(models.Model):
    used_in=models.CharField(max_length=100,blank=True,null=True)
    category=models.ForeignKey(category,max_length=50,on_delete=models.CASCADE)
    amount=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.name