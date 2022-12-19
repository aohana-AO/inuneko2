import requests
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Health
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

import requests

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html',)

class CreatePost(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        return render(request, 'app/post_form.html', {
            'form': form
        })


    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Health()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.category = form.cleaned_data['category']


            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', post_data.id)

        return render(request, 'app/post_form.html', {
            'form': form
        })

class PostDetailView(View):
        def get(self, request, *args, **kwargs):
            user = request.user
            post_data = Health.objects.get(id=self.kwargs['pk'])
            return render(request, 'app/post_detail.html', {'post_data': post_data, 'user': user})

class PostDeleteView(View):
    def get(self, request, *args, **kwargs):
        post_data = Health.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {'post_data': post_data})

    def post(self, request, *args, **kwargs):
        post_data = Health.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')

class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Health.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'content': post_data.content,
                'author': post_data.author,
                'category': post_data.category,


            }

        )
        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Health.objects.get(id=self.kwargs['pk'])
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.category = form.cleaned_data['category']

            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_form.html', {
            'form': form
        })

class APItati(View):
    def inu(request):
        url = 'https://dog.ceo/api/breeds/image/random'
        # url = 'https://random.dog/doggos/image/random'
        get_result = requests.get(url).json()
        result = [get_result]
        print(result)

        return render(request, 'app/inu.html', {
        'result': result
    })
    def sibainu(request):
        import requests

        url = 'http://shibe.online/api/shibes?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]'
        get_result = requests.get(url).json()
        result = ["https://cdn.shibe.online/shibes/" + get_result[0] + ".jpg"]
        print(result)
        return render(request, 'app/sibainu.html', {
            'result': result
        })

