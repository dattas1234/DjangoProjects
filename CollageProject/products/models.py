from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


class Offer(models.Model):
    product= models.ManyToManyField(Product)
    code=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    discount= models.CharField(max_length=20)
    #validtill=models.DateTimeField(auto_now= False, auto_now_add=False, default=default_date())
    
class Cart(models.Model):
    productId=models.CharField(max_length=20)
    quantity=models.IntegerField(max_length=20)

#def default_date():
 #   date= datetime.today()
  #  return date.date()

# class Order(models.Model):
#     name