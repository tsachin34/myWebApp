from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView, ListView, FormView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BookDetail
from .forms import AddBookForm, UpdateBookForm
from users.models import User


# Create your views here.


class BookListView(FormView, TemplateView):
    model = BookDetail
    template_name='books/add_books.html'
    form_class= AddBookForm

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
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
        user=User.objects.filter(user__pk=self.kwargs['pk']).first()
       
        if 'add_book_form' in request.POST:
            
            add_book_form = AddBookForm(request.POST,request.FILES)
            if add_book_form.is_valid():
                
                book=add_book_form.save(self.request.user)
            else:
                
                context['add_book_form']=add_book_form

        if 'update_book_form' in request.POST:
            update_book_form=UpdateBookForm(request.POST,request.FILES)
            if update_book_form.is_valid():
                book=BookDetail.objects.filter(pk=self.kwargs['slug'])
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




# class BookDetailView():
#     model = BookDetailk
#     form_class = CreatePostForm
#     template_name = 'forum/post_detail.html'

#     def get_context_data(self, **kwargs):
#         post = Post.objects.filter(pk=self.kwargs['pk']).first()
#         comments = Comment.objects.filter(post = post)

#         post_image = PostImage.objects.filter(post = post).first()
#         print(post_image)
#         liked_post = PostLike.objects.filter(liked_post=self.kwargs['pk'], liker_user = self.request.user).first()
#         if liked_post != None:
#             liked_post = liked_post.liked
#         context =  super(PostDetailView, self).get_context_data(**kwargs)
#         context['post'] = post
#         context['comments'] = comments
#         context['post_image'] = post_image
#         context['liked_post'] = liked_post

#         if 'comment_form' not in context:
#             context['comment_form'] = AddCommentForm()

#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         context = {}

#         current_post = Post.objects.filter(pk=self.kwargs['pk']).first()

#         if 'add_comment' in request.POST:
#             add_comment_form = AddCommentForm(request.POST)

#             if add_comment_form.is_valid():
#                 add_comment_form.save(current_post, self.request.user)
#             else:
#                 context['comment_form'] = add_comment_form
        
#         if 'like_post' in request.POST:
#             current_post.like_post()
#             liked_post = PostLike.objects.filter(liked_post=current_post, liker_user = self.request.user).first()
#             if liked_post == None:
#                 liked_post = PostLike.objects.create(liked_post=current_post, liker_user = self.request.user)
#                 liked_post.is_liked()
#             else:
#                 liked_post.is_liked()
            
        
#         if 'dislike_post' in request.POST:
#             current_post.dislike_post()
#             liked_post = PostLike.objects.filter(liked_post=current_post, liker_user = self.request.user).first()
#             liked_post.not_liked()
        
#         if 'like_comment' in request.POST:
#             current_comment = Comment.objects.filter(pk=request.POST['comment_data']).first()
#             current_comment.like_comment()
#             liked_comment = CommentLike.objects.filter(liked_comment=current_comment, liker_user = self.request.user).first()
#             if liked_comment == None:
#                 liked_comment = CommentLike.objects.create(liked_comment=current_comment, liker_user = self.request.user)
#                 liked_comment.is_liked()
#             else:
#                 liked_comment.is_liked()

#         if 'dislike_comment' in request.POST:
#             current_comment = Comment.objects.filter(pk=request.POST['comment_data']).first()
#             current_comment.dislike_comment()
#             liked_comment = CommentLike.objects.filter(liked_comment=current_comment, liker_user = self.request.user).first()
#             liked_comment.not_liked()
        
#         return render(request, self.template_name, self.get_context_data(**context))



 




