from django.db import models

# Create your models here.

class members(models.Model):
    member_id=models.IntegerField(auto_created=True,primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=128)
    username=models.CharField(max_length=30)
        

FURNISHING_CHOICES = (
    ('N/A','N/A'),
   ('Furnished', 'Furnished'),
   ('Not Furnished', 'Not Furnished'),
   ('Semi Furnished', 'Semi Furnished')
   
)

class property(models.Model):
    owner_id = models.ForeignKey(members, on_delete=models.DO_NOTHING)
    property_id=models.IntegerField(auto_created=True,primary_key=True)
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    location = models.CharField(max_length=50)
    image = models.FileField(max_length=100,upload_to="property_images/",null=True,default=None)
    area=models.IntegerField()
    description = models.TextField()
    title=models.CharField(max_length=30)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    action=models.CharField(max_length=30,default='sell')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    name=models.CharField(max_length=30)
    bedrooms=models.IntegerField(blank=True,null=True)
    bathrooms=models.IntegerField(blank=True,null=True)
    furnished = models.CharField(choices=FURNISHING_CHOICES, max_length=128)
    contact=models.IntegerField()
    owner_email=models.EmailField(max_length=30)
    
    
class Enquiry(models.Model):
    sender_id=models.ForeignKey(members, on_delete=models.DO_NOTHING)
    reciever_id=models.CharField(max_length=20)
    property=models.ForeignKey(property, on_delete=models.DO_NOTHING)
    message=models.CharField(max_length=50)
    sender_name=models.CharField(max_length=30)
    sender_contact=models.IntegerField()
    posted_on=models.DateField(auto_now_add=True)
    
class Agents(models.Model):
    agent_id=models.IntegerField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20,default=123)
    email=models.EmailField(max_length=40)

class AgentsInfo(models.Model):
    agent_id=models.ForeignKey(Agents,on_delete=models.DO_NOTHING)
    agent_name=models.CharField(max_length=30)
    agent_contact=models.IntegerField()
    agent_email=models.EmailField(max_length=40)
    joined_on=models.DateField(auto_now_add=True)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    operating_city=models.CharField(max_length=50)
    operating_locations=models.CharField(max_length=50)
    deals_in=models.CharField(max_length=60)
    image = models.FileField(max_length=100,upload_to="agent_images/")
    operating_since=models.IntegerField(default=2015)

class Contact_User(models.Model):
    member_id=models.ForeignKey(members,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=30)
    message=models.TextField()
    contact=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
