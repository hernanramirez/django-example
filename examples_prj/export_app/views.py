from export_app.forms import ContactForm
from django.views.generic.edit import FormView


class BookSearchView(FormView):
    template_name = 'export_app/book_search.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super(BookSearchView, self).form_valid(form)
