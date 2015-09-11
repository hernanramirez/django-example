from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import openpyxl
from django.views.generic import TemplateView
from import_app.models import Book

from import_app.models import FileImport


class FileMixin(object):
    model = FileImport


class FileList(FileMixin, ListView):
    template_name = 'import_app/file_list.html'


class FileUpdate(UpdateView):
    success_url = reverse_lazy('file_list')


class FileNew(FileMixin, CreateView):
        template_name = 'import_app/file_new.html'
        success_url = reverse_lazy('file_list')

class FileDelete(FileMixin, CreateView):
        template_name = 'import_app/file_confirm_delete.html'
        success_url = reverse_lazy('file_list')


class ImportView(TemplateView):
    template_name = "import_app/import_view.html"

    def get_context_data(self, **kwargs):
        context = super(ImportView, self).get_context_data(**kwargs)

        workbook = openpyxl.load_workbook(filename = '/home/hernanr/myCode/python/Rene/importar/b.xlsx', use_iterators = True)
        worksheet = workbook.get_sheet_by_name('Sheet1')

        context['data2'] = Book.objects.all()

        d = []

        for row in worksheet.iter_rows():
            

            
            data = {'a': row[0].value,
                    'b': row[1].value,
                    'c': row[2].value,
                    'd': row[3].value,
            }
            d.append(data)

	    #print data['my_first_col'], '::', data['my_second_col'], '::', data['my_third_col']

        context['data'] = d

        # if self.request.user.is_authenticated():
        #    context['planilla'] = Pasante.objects.get(user=self.request.user)

        return context
