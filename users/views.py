from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView
from users.models import User
from .forms import CustomUserCreationForm, EditUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class EditUserView(LoginRequiredMixin, FormView):
    model = User
    template_name = 'edit_user.html'
    form_class = EditUser
    success_url = reverse_lazy('home')
    raise_exception = True

    def form_valid(self, form):
        update_info = User.objects.filter(id=self.request.user.id)
        update_info.update(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            phone_number=form.cleaned_data['phone_number'],
        )
        return super(EditUserView, self).form_valid(form)

    def get_initial(self):
        initial = super(EditUserView, self).get_initial()
        if self.request.user.is_authenticated:
            initial['first_name'] = self.request.user.first_name
            initial['last_name'] = self.request.user.last_name
            initial['phone_number'] = self.request.user.phone_number
        return initial
