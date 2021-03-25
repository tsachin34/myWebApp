from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, FormView, DetailView, TemplateView
# Create your views here.
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import UserForm

from .models import User

from books.forms import AddBookForm, UpdateBookForm
from books.models import BookDetail




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


class ProfileView(FormView, TemplateView):
    model = BookDetail
    template_name='users/user_profile.html'
    form_class= AddBookForm

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        books = BookDetail.objects.all()
        context['books']=books
        if 'add_book_form' not in context:
            context['add_book_form'] = AddBookForm()
        if 'update_book_form' not in context:
            context['update_book_form']=UpdateBookForm()
        return context
         

   
    def post(self,request, *args, **kwargs):
        
        context={

        }
        user=User.objects.filter(username=self.kwargs['slug']).first()
        print(user)
        if 'add_book_form' in request.POST:
            
            add_book_form = AddBookForm(request.POST,request.FILES)
            if add_book_form.is_valid():
                
                book=add_book_form.save(self.request.user)
            else:
                
                context['add_book_form']=add_book_form

        if 'update_book_form' in request.POST:
            update_book_form=UpdateBookForm(request.POST,request.FILES)
            if update_book_form.is_valid():
                book=BookDetail.objects.filter(pk=self.kwargs['pk'])
                update_book_form.save(book)

            else:
                context['update_book_form']= update_book_form


        
        return render(request, self.template_name, self.get_context_data(**context))

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            search_query = request.GET.get('search_box', None)
            queryset = []
            for i in BookDetail.objects.all():
                if search_query:
                    if i.title.find(search_query) != -1:
                        queryset.append(i)
            self.posts = queryset
        return render(request, self.template_name, self.get_context_data())



def deleteBook(request,slug,pk):
    book = BookDetail.objects.get(id=pk)
    book.delete()
    return redirect('users:userprofile',slug=slug)


class BookDetailsView(FormView, TemplateView):
    modal = BookDetail
    template_name='users/book_details.html'
    form_class = UpdateBookForm

    def get_context_data(self, **kwargs):
        context = super(BookDetailsView, self).get_context_data(**kwargs)
        book = BookDetail.objects.filter(pk=self.kwargs['pk']).first()
        context['book']=book
        if 'update_book_form' not in context:
            context['update_book_form']=UpdateBookForm()
        return context

    
    def post(self,request, *args, **kwargs):
        
        context={

        }
        user=User.objects.filter(username=self.kwargs['slug']).first()
        print(user)

        if 'update_book_form' in request.POST:
            update_book_form=UpdateBookForm(request.POST,request.FILES)
            if update_book_form.is_valid():
                book=BookDetail.objects.filter(pk=self.kwargs['pk']).first()
                print("Hello 4367456354")
                print(book)
                update_book_form.save(book)

            else:
                context['update_book_form']= update_book_form


        
        return render(request, self.template_name, self.get_context_data(**context))

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            search_query = request.GET.get('search_box', None)
            queryset = []
            for i in BookDetail.objects.all():
                if search_query:
                    if i.title.find(search_query) != -1:
                        queryset.append(i)
            self.posts = queryset
        return render(request, self.template_name, self.get_context_data())
    
