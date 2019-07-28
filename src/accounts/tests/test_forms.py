from django.test import TestCase
from ..forms import (
    UserRegisterForm, EditProfileForm, 
    RoleCreationForm, EditRoleForm
)

class UserCreationFormTest(TestCase):
    
    def setUp(self):
        self.user_register = UserRegisterForm()
        self.user_register2 = UserRegisterForm(
            data={
                'username': 'anyric',
                'email': 'anyric@info.com',
                'password1': 'anyric@1234',
                'password2': 'anyric@1234'
            }
        )

    def test_username_field_label(self):
        self.assertFalse(self.user_register.fields['username'].label == None)
        self.assertTrue(self.user_register.fields['username'].label == 'Username')
    
    def test_email_field_label(self):
        self.assertTrue(self.user_register.fields['email'].label == None)
        self.assertFalse(self.user_register.fields['email'].label == 'Email')

    def test_password_field_label(self):
        self.assertFalse(self.user_register.fields['password1'].label == None)
        self.assertTrue(self.user_register.fields['password1'].label == 'Password')
        self.assertFalse(self.user_register.fields['password2'].label == None)
        self.assertTrue(self.user_register.fields['password2'].label == 'Confirm Password')

    def test_is_admin_field_label(self):
        self.assertFalse(self.user_register.fields['is_admin'].label == None)
        self.assertTrue(self.user_register.fields['is_admin'].label == 'Is Admin')

    def test_form_is_valid(self):
        self.assertTrue(self.user_register2.is_valid())

    def test_form_is_not_valid(self):
        self.assertFalse(self.user_register.is_valid())


class EditProfileFormTest(TestCase):
    
    def setUp(self):
        self.user_edit = EditProfileForm()
        self.user_edit2 = EditProfileForm(
            data={
                'username': 'anyric',
                'email': 'anyric@info.com',
                'password': 'anyric@1234'
            }
        )
    def test_username_field_label(self):
        self.assertFalse(self.user_edit.fields['username'].label == None)
        self.assertTrue(self.user_edit.fields['username'].label == 'Username')
    
    def test_email_field_label(self):
        self.assertFalse(self.user_edit.fields['email'].label == None)
        self.assertFalse(self.user_edit.fields['email'].label == 'Email')

    def test_password_field_label(self):
        self.assertTrue(self.user_edit.fields['password'].label == None)
        self.assertFalse(self.user_edit.fields['password'].label == 'Password')

    def test_form_is_not_valid(self):
        self.assertFalse(self.user_edit.is_valid())


class RoleCreationFormTest(TestCase):
    
    def setUp(self):
        self.role_creater = RoleCreationForm()
        self.role_creater2 = RoleCreationForm(
            data={
                'name': 'test',
                'description': 'This is a test role'
            }
        )

    def test_role_name_field_label(self):
        self.assertFalse(self.role_creater.fields['name'].label == None)
        self.assertFalse(self.role_creater.fields['name'].label == 'name')
    
    def test_role_description_field_label(self):
        self.assertFalse(self.role_creater.fields['description'].label == None)
        self.assertFalse(self.role_creater.fields['description'].label == 'description')

    def test_form_is_valid(self):
        self.assertTrue(self.role_creater2.is_valid())

    def test_form_is_not_valid(self):
        self.assertFalse(self.role_creater.is_valid())


class RoleEditFormTest(TestCase):
    
    def setUp(self):
        self.role_creater = EditRoleForm()
        self.role_creater2 = EditRoleForm(
            data={
                'name': 'test2',
                'description': 'This is a test2 role'
            }
        )

    def test_role_name_field_label(self):
        self.assertFalse(self.role_creater.fields['name'].label == None)
        self.assertFalse(self.role_creater.fields['name'].label == 'name')
    
    def test_role_description_field_label(self):
        self.assertFalse(self.role_creater.fields['description'].label == None)
        self.assertFalse(self.role_creater.fields['description'].label == 'description')
    
    def test_form_is_valid(self):
        self.assertTrue(self.role_creater2.is_valid())

    def test_form_is_not_valid(self):
        self.assertFalse(self.role_creater.is_valid())

