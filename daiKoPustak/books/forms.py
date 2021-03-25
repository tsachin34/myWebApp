from django.db.models import fields
from django.forms import ModelForm
from .models import BookDetail, Bid
from django.core.files.base import ContentFile, File 
import os
import urllib.request

class AddBookForm(ModelForm):
    class Meta:
        model= BookDetail
        exclude=('posted_date','likes','author')
            
        


    def save(self,user):
        book= BookDetail.objects.create(
            title=self.cleaned_data['title'],
            description= self.cleaned_data['description'],
            author=user,
            purchased_on=self.cleaned_data['purchased_on'],
            image=self.cleaned_data['image'],
        )
        print(book.image)
        return book


class UpdateBookForm(ModelForm):

    class Meta:
        exclude=('posted_date','likes','author')
        model=BookDetail

    def save(self,book):
        book.title=self.cleaned_data['title']
        book.text_content=self.cleaned_data['description']
        book.purchased_on=self.cleaned_data['purchased_on']
        book.image.save(os.path.basename(book.image.url), File(self.cleaned_data['image']), save=False) 
        book.save()
        
        return book

    

class AddBidForm(ModelForm):
    class Meta:
        exclude =('bidder','book')
        model= Bid

    def save(self,book,bidder):
       bid = Bid.objects.create(
        book=book,
        bidder=bidder,
        amount=self.cleaned_data['amount']
       )

