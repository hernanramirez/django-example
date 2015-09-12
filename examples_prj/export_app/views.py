from export_app.forms import ContactForm
from export_app.resource import BookResource
from export_app.models import Book
from django.views.generic.edit import FormView
from django.http import HttpResponse
from pure_pagination.mixins import PaginationMixin
from django.views.generic.list import ListView


class BookMixin(object):
    model = Book


class BookList(BookMixin, PaginationMixin, ListView):

    template_name = 'export_app/books/object_list.html'

    page = {
        'title': 'Dispositivos',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class BookSearchView(FormView):
    template_name = 'export_app/book_search.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']
        q = Book.objects.filter(published__gte=d, published__lte=h)
        dataset = BookResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=prospectExport.xls'
        return response


class BookModalExportView(FormView):
    template_name = 'export_app/book_export.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']
        q = Book.objects.filter(published__gte=d, published__lte=h)
        dataset = BookResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=prospectExport.xls'
        return response

    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(BookSearchView, self).form_valid(form)
