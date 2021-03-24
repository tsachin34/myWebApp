from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django.db.transaction import commit
import random

class UserForm(UserCreationForm):
   

    class Meta:
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','education')

        @transaction.atomic()
        def save(self):
            user = User.objects.create(
                education=self.cleaned_data['education'],
                slug=self.cleaned_data['username']

            )
            return user