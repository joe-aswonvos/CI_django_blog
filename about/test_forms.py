from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Testy McTestface',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
    def test_form_name_is_invalid(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name field permits empty string")
        
    def test_form_email_is_invalid(self):
        form = CollaborateForm({
            'name': 'Testy McTestface',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="email field permits empty string")
        
    def test_form_message_is_invalid(self):
        form = CollaborateForm({
            'name': 'Testy McTestface',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message field permits empty string") 