from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True