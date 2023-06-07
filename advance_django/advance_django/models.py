from django.db import models 



class Comments(models.Model):
    title=models.CharField(max_length=120,verbose_name="نام")
    email=models.EmailField(max_length=300,verbose_name="ایمیل")
    status=models.BooleanField(default=True)