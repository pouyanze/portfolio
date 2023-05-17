from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from contact.models import Contact
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            messages.success(request, 'Your message has been sent.', extra_tags='success-contact') # Add a success message
            return redirect('contact')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the errors in the form.')
            return render(request, 'contact/contact.html', {'form': form, 'errors': form.errors})


class MessageListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Contact
    template_name = 'contact/view_messages.html'
    context_object_name = 'messages'
    paginate_by = 10
    def test_func(self):
        return self.request.user.is_superuser
    

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('view_messages')

    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        # Delete the message object
        self.object.delete()

        return HttpResponseRedirect(success_url)