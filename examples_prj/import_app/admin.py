from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_app.models import Category, Author, Book


class BookResource(resources.ModelResource):

    class Meta:
        model = Book


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    pass


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
