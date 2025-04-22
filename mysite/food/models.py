from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    def __str__(self):
        return self.Item_name
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Item_name=models.CharField(max_length=50)
    Item_desc=models.CharField(max_length=200)
    Item_price=models.IntegerField()
    Item_image=models.CharField(max_length=500, default="https://www.shutterstock.com/image-photo/restaurant-blackboard-announcing-reopening-after-600nw-1735273409.jpg")
    
    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})
