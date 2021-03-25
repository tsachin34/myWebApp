from django.db import models

from users.models import User

# Create your models here.
class BookDetail(models.Model):

    title = models.CharField(max_length=200, default=None)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    purchased_on=models.DateField()
    likes = models.PositiveIntegerField(default=0)
    image= models.ImageField(upload_to='books_img',default='images/book-open.png')
    posted_date = models.DateTimeField(auto_now_add=True)
    

    def like_post(self):
        self.likes += 1
        self.save()
    
    def dislike_post(self):
        self.likes -= 1
        self.save()

    def __str__(self):
        return self.title


class Bid(models.Model):
    book= models.ForeignKey(BookDetail,on_delete=models.CASCADE)
    bidder= models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.book) +" " + str(self.amount)
    