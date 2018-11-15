from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=20)


    #함수를 재정의 오버라이딩 !
    def __str__(self):
        return self.address