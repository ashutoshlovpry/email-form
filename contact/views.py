from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
# if request.method == 'POST':
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         form.send()
#         return redirect('contact:success')
# else:
#     form = ContactForm())
class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'