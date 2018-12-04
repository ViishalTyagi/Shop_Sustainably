from django.db import models
import os
import random

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def uplpoad_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3245621256)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename, 
        final_filename=final_filename
        )

class ProductManager(models.Model):
    def get_by_id(self, id):
        return self.get_queryset().filter(id=id)

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True) #add default = 100.00 or null = True
    image = models.ImageField(upload_to= uplpoad_image_path, null =True, blank = True)
    featured =models.BooleanField(default=False)
    
    objects = ProductManager()

    def __str__(self):
        return self.title