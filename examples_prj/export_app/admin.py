from django.contrib import admin
from export_app.models import Category, Book, Author


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)