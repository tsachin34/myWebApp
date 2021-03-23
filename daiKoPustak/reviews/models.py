from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    

    user = models.ForeignKey(User,related_name="user_profile",on_delete=models.CASCADE)
    reviwer= models.ForeignKey(User,related_name='reviewer',on_delete=models.CASCADE)
    published_date= models.DateTimeField(default=timezone.now)
    ratings = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    # richtextfield to give editing options in editor
    description = models.CharField(max_length=256,blank=True,default='',null=True)


    def __str__(self):
        return self.description

    

