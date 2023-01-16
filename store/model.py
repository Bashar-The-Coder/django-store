from django.db import models

#many to many relationtship-24
# we can define many to many relationship between
# a products can have different promotion
# and a promotion can apply differnt product
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    # circular dependency with product class
    # if we delete a product and that product has 
    # featured product for collection here we set field to null
    # here we create reverse relationship thats why we face clash on same name in product and collection class
    # so we need to add related name 
    featured_product = models.ForeignKey ('Product', on_delete= models.SET_NULL, null= True , related_name= "+")

# Create your models here.
class Product(models.Model):
    sku = models.CharField (max_length=10, primary_key= True)
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = models.TextField ()
    price = models.DecimalField(max_digits=6 , decimal_places=2) # float has rounding issue. so we use decimal fielld
    inventory  = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    #sometimes we cant arrange our code before or after relationship
    # so we can identify our relationship with models name with string quotation
    collection = models.ForeignKey('Collection', on_delete= models.PROTECT)
    promotions = models.ManyToManyField(Promotion, related_name='products')
    
class Customer (models.Model): 
    MEMBER_BRONZE = "B"
    MEMBER_SILVER = ""
    MEMBER_GOLD= "B"
    MEMBERSHIP_CHOICES = [
        (MEMBER_BRONZE ,    'Bronze'),
        (MEMBER_SILVER ,    'Silver'),
        (MEMBER_GOLD ,      'Gold'),
    ]
    first_name = models.CharField(max_length=  255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField (unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 , choices=MEMBERSHIP_CHOICES , default= MEMBER_BRONZE)
    
    # class Meta:
    #     db_table = 'store_customers'
    #     indexes = [models.Index(fields=['last_name', 'first_name'])]
    
    
class Order(models.Model):
    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"
    
    payment_status_choices = [
        (PAYMENT_PENDING , "Pending"),
        (PAYMENT_COMPLETE , "Complete"),
        (PAYMENT_FAILED , "Failed"),
            ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1, choices= payment_status_choices, default= PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # here if we delete a customer we dont want to delete our order sales
    
class OrderItem(models.Model):
    sku = models.CharField()
    order = models.ForeignKey(Order, on_delete= models.PROTECT)
    product = models.ForeignKey(Product, on_delete= models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer , on_delete=models.CASCADE , primary_key = True)
    # here customer is the parent and address is child class
    # on_delete cascade mean when we delete customer then address will be deleted
    # on_delete models.Protect mean we should delete child property then we delete parent
    # if we not set primary key = True then django will create an id field and place the id as primary key
    # As a result then every address has an id and that means we gonna end up with one to many relationship between customer and addresses
    # if we set primary key then it allow one customer with one address coz primary key doesn't allow duplicate value
    # we dont need to define reverse relationship in customer class coz django automatically create that process
    zips = models.CharField(max_length=100, null= True, blank= True)
######## one to many relationship lesson 23 £££££££

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()