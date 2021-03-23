from django.urls import path, re_path

from . import views

app_name="books"


urlpatterns = [
    re_path(r'^add_books/(?P<pk>[-\w]+)/$',views.BookListView.as_view(),name="add")
    
]