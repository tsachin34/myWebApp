from django.db.models import fields
from django.forms import ModelForm
from .models import BookDetail


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
        book.image=self.cleaned_data['image'],
        book.save()

        return book

    