from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creats a custom user with no privilages
    form a provided email and password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        #del self.fields['username']

    class Meta:
        model = UserProfile 
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    #def __init__(self, *args, **kargs):
        #super(CustomUserChangeForm, self).__init__(*args, **kargs)
        #del self.fields['username']
        

    class Meta:
        model = UserProfile 
        fields = '__all__'

