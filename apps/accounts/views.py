from django.contrib.auth import forms
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.safestring import mark_safe
import markdown
from django import template

register = template.Library()



class CustomLoginView(LoginView):
    form_class = forms.LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_data"] = self.form_class()
        return context


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = forms.UpdateUserForm(request.POST, instance=request.user)
        profile_form = forms.UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = forms.UpdateUserForm(instance=request.user)
        profile_form = forms.UpdateProfileForm(instance=request.user.profile)

    return render(request, 'registration/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-profile')



