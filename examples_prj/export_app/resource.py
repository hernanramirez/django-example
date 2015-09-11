from import_export import resources
from export_app.models import Book
from import_export import fields


class BookResource(resources.ModelResource):

    #author = fields.Field(column_name='author__name')

    class Meta:
        model = Book
        fields = ('id', 'name','author__name', 'price','published',)
        widgets = {
                'published': {'format': '%d/%m/%Y'},
                }
