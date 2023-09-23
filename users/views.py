from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

# from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Store - Регистрация'


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'

    def get_success_url(self) -> str:
        return reverse_lazy('products:index')


class UserLogoutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('products:index')
