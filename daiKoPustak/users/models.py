from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):

    #ENUM field for the education level choices
    EDU_CHOICES=(
        (1,'School'),
        (2,'High School'),
        (3,'Bachelors Level'),
        (4,'Masters Level')
    )


    education= models.PositiveBigIntegerField(choices=EDU_CHOICES,blank=True,null=True)

    def __str__(self):
        return self.username

# admin.site.register()



