from django.db import models
#this contentype model specificly made us allow to create generic relationship
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)
    

class TaggedItem(models.Model):
        #what tag is applied to what object
        # if we delete tag then associate item should be deleted
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
    # for this we need to import product object from store.models 
    # but what if we need to tag item someday is about video , Articles?
    # as this is totally different app we dont want to depend specific
    # models
    
    # product = models.ForeignKey(Product)
    
    # here we need to identify genericly our object 
    # to do that we need two piece of information
    # first type of object like product, video, article
    # second we need to id on those object
    # by this two info we can identify any object of our  application
    # of in database terms any record 
    # for this instead of using concrete model like product
    # we should use generic way to create  a model
    # with the setting contenttype we can define generic
    # relactionship with our model.
    # instead of create product model we can use
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey
    
    #  to define generic relationship we need this three field