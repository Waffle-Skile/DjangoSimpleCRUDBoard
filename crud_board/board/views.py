from django.contrib import messages
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {
            'post_num': len(Post.objects.all()),
            'recent_posts': Post.objects.order_by('-created_at')[:3],
        }


class PostView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"

    fields = ['title', 'content', 'author', 'password']


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"

    fields = ['title', 'content', 'author']

    def post(self, request, *args, **kwargs):
        if request.POST.get('pw', '') == self.get_object().password:
            return super().post(self, request, *args, **kwargs)
        else:
            messages.info(request, 'Wrong password. Update failed.')
            return HttpResponseRedirect(reverse('post-detail', kwargs={
                'pk': self.get_object().pk}))


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"

    def get_success_url(self):
        return reverse('index')

    def delete(self, request, *args, **kwargs):
        if request.POST.get('pw', '') == self.get_object().password:
            return super().delete(self, request, *args, **kwargs)
        else:
            messages.info(request, 'Wrong password. Deletion failed.')
            return HttpResponseRedirect(reverse('post-detail', kwargs={
                'pk': self.get_object().pk}))
