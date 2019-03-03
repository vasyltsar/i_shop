from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView
from users.models import User
from .forms import CustomUserCreationForm, EditUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class EditUser(FormView):
    model = User
    template_name = 'edit_user.html'
    form_class = EditUserCreationForm
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super(EditUser, self).get_initial()
        if self.request.user.is_authenticated:
            print(self.request)
            initial['first_name'] = self.request.user.first_name
            initial['last_name'] = self.request.user.last_name
            initial['phone_number'] = self.request.user.phone_number
        return initial
