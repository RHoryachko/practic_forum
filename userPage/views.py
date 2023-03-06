from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Profile
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.db import IntegrityError

'''
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return context
'''

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/user_profile.html'
    # Використовуємо reverse_lazy() для того, щоб уникнути проблем з імпортуванням URL-адреси
    # під час ініціалізації класу.
    create_profile_url = reverse_lazy('create_user_profile')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return redirect(self.create_profile_url)
        return super().get(request, *args, **kwargs)



class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'profile/create_profile.html'
    fields = ['profile_pic', 'bio', 'first_name', 'last_name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            self.object = form.save()
        except IntegrityError:
            # Profile already exists for this user, update it instead
            self.object = Profile.objects.get(user=self.request.user)
            form.instance.id = self.object.id  # set the ID to update the existing instance
            form.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('post_list')


    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].widget.attrs.update({'class': 'real-input'})
        form.fields['last_name'].widget.attrs.update({'class': 'real-input'})
        form.fields['bio'].widget.attrs.update({'class': 'add-bio', 'placeholder': 'Enter your bio...'})
        return form


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'profile/edit_user_profile.html'
    fields = ['profile_pic', 'bio', 'first_name', 'last_name']

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('post_list')

    def get_initial(self):
        initial = super().get_initial()
        profile = self.get_object()
        initial['bio'] = profile.bio
        initial['first_name'] = profile.first_name
        initial['last_name'] = profile.last_name
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].widget.attrs.update({'class': 'real-input'})
        form.fields['last_name'].widget.attrs.update({'class': 'real-input'})
        form.fields['bio'].widget.attrs.update({'class': 'add-bio', 'placeholder': 'Enter your bio...'})
        return form