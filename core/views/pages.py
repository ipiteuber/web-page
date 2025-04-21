from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

# Paginas protegidas exclusivas para uso de usuario autenticados

class ServicesView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'index/services.html'

    def test_func(self):
        return not self.request.user.is_staff

class CartView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'index/cart.html'

    def test_func(self):
        return not self.request.user.is_staff

class ProfileView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'account/profile.html'

    def test_func(self):
        return not self.request.user.is_staff

class WelcomeLogView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'account/welcome_log.html'

    def test_func(self):
        return not self.request.user.is_staff
