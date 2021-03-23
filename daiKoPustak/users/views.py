from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import UserForm




def signUpView(request):
    if request.method == 'POST':
    

        user_form =UserForm(request.POST)

        if user_form.is_valid():
            # user = user_form.save(commit=False)
            user_form.save()

            return HttpResponseRedirect(reverse_lazy("users:login"))
        else:
            context={
                'user_form':user_form
            }

    else:
        context = {
            'user_form': UserForm(),
            
        }

    return render(request, 'users/signup.html', context)


class HomePage(TemplateView):
    template_name='users/index.html'