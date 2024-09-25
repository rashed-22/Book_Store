from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
#For class based view and template
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

#Function Based View
# def home(request):
#     return render(request, 'home.html')


#class Based Template View
class MyTemplateViews(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'Rahim', 'age': 22}
        print(context)
        context.update(kwargs)
        print(context)
        return context

# def store_book(request):
#     if request.method == "POST":
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             return redirect('showbook')
#     else:
#         book = BookStoreForm()
#     return render(request, 'store_book.html', {'form': book})


#Class based Form view
class BookFormView(FormView):
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return redirect('showbook')
    
#Class based Create view
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')
    
    

# def show_book(request):
#     book = BookStoreModel.objects.all()
#     print(book)
#     return render(request,'show_book.html', {'data': book})

#Class based List view
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'data'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author='abc')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'abc': BookStoreModel.objects.all().order_by('author')}
    #     return context
    ordering = ['id']
    
#Class based Details view
class BookDetailView(DetailView):
    model = BookStoreModel
    template_name = 'book_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

# def edit_book(request, id):
#     book = BookStoreModel.objects.get(pk=id)
#     form = BookStoreForm(instance= book)
#     if request.method == "POST":
#         form = BookStoreForm(request.POST, instance= book)
#         if form.is_valid():
#             form.save()
#             return redirect('showbook')
#     return render(request,'store_book.html', {'form': form})

#Class based Update view
class BookUpdate(UpdateView):
    form_class = BookStoreForm
    model = BookStoreModel
    template_name = 'store_book.html'
    success_url = reverse_lazy('showbook')
    

# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk=id).delete()
#     return redirect('showbook')

#Class based Delete view
class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = 'delete.html'
    success_url = reverse_lazy('showbook')



    