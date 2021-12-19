from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class UserProfile(models.Model):
    id = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False
                    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)#username,email etc.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    birthday = models.DateField()

    def __str__(self):
        return str(self.user.username)


class Category(models.Model):
    """ Product has a category """
    id = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False
                    )
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)
    

class Tag(models.Model):
    id = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False
                    )
    """ Product has tag. For a better search operation """
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    id = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False
                    )
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)
    price = models.PositiveIntegerField()
    category = models.ManyToManyField(Category,related_name="product_categories")
    tags = models.ManyToManyField(Tag,related_name="product_tags")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)
    #thumbnail = models.ImageField(upload_to="images/",blank=True,null=True)

    def __str__(self):
        return str(self.name)
    
    def get_thumbnail(self,instance):
        images = instance.objects.filter(product=self)
        for image in images:
            if image.is_thumbnail:
                return image.image

        



class Comment(models.Model):
    """ Product has comment. To give an idea to users """
    id = models.UUIDField(
                    primary_key=True,
                    default=uuid.uuid4,
                    editable=False
                    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return str(self.comment)[:20]
    

    

class Point(models.Model):
    """ Product has point that given by users """
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(default=5, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f"{self.user.username} : {self.product.name} -> {self.value}"

class ProductImage(models.Model):
    """ Products can have multiple images """
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images/")
    is_thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return f" image for {self.product.name}"

class Basket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,related_name="products_in_basket")

    def __str__(self):
        return f"{self.user}"
