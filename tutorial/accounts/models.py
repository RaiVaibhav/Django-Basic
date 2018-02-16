from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# user model is like where all the data is gets stored/save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default ='')
    city = models.CharField(max_length =100, default ='')
    website = models.URLField(default ='')
    phone = models.IntegerField(default=0)

    #problems with model is everytime we have to manually add the user in data to solve that we use the django signals
    #to trigger the code


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])
        #what it will do it whenever any new user create a accounnt UserProfile get to about it automatically
        # i.e. UserProfile will have its object

post_save.connect(create_profile, sender= User)