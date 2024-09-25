from django.urls import path
# from book.views import home, store_book, show_book, edit_book, delete_book
from . import views

urlpatterns = [
    path('', views.MyTemplateViews.as_view(template_name = 'home.html'), {'author': 'Muni'}),
    # path('store_new_book/', views.store_book, name="storebook"),
    path('store_new_book/', views.BookFormView.as_view(), name="storebook"),
    path('show_books/', views.BookListView.as_view(), name="showbook"),
    path('detail_books/<int:id>', views.BookDetailView.as_view(), name="detailbook"),
    # path('edit_book/<int:id>', views.edit_book, name="editbook"),
    path('edit_book/<int:pk>', views.BookUpdate.as_view(), name="editbook"),

    # path('delete_book/<int:id>', views.delete_book, name="deletebook"),
    path('delete_book/<int:pk>', views.BookDeleteView.as_view(), name="deletebook"),

]