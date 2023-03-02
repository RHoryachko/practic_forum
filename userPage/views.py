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


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return context


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