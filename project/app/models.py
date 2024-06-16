from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    descripition=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
@receiver(post_save,sender=Product)
def product_update(sender,instance, **kwargs):
    print(f'Product is created at:{instance.created_at}')


