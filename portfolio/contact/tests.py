from django.test import TestCase
from django.urls import reverse

from contact.models import Contact

class ContactAppTests(TestCase):
    def test_contact_form_submission(self):
        # Create a test contact form data
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'Test message',
        }

        # Submit the contact form
        response = self.client.post(reverse('contact'), form_data)

        # Check that the form submission was successful
        self.assertEqual(response.status_code, 302)  # Redirect response
        self.assertRedirects(response, reverse('contact'))

        # Check that the contact object was created in the database
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, form_data['name'])
        self.assertEqual(contact.email, form_data['email'])
        self.assertEqual(contact.message, form_data['message'])
