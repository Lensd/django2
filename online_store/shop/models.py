from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(unique=True)
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('shop.Brand', on_delete=models.CASCADE)
    thumb = models.ImageField(default='default_product.png', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_brands'


class Slide(models.Model):
    image = models.ImageField(default='slide.jpg')


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    total_price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"{self.product} x{self.amount} - {self.order.customer.username}"


RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Excellent'),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, max_length=3000)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return self.user.username
