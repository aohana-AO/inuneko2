import math
from django.contrib.auth.models import User
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
        user = request.user
        post_data = Health.objects.order_by('-id')
        form = PostForm(request.POST or None)
        return render(request, 'app/index.html', {
            'post_data': post_data, 'form': form, 'user': user
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        print(1)
        print(2)
        problemcategory = request.POST["problemcategory"]
        print(problemcategory)
        purpose = request.POST["purpose"]
        print(purpose)
        status = request.POST["status"]
        print(status)
        problemsize = request.POST["problemSize"]
        print(problemsize)
        organization = request.POST["organization"]
        print(organization)
        post_data = Health.objects.filter(problemCategory=problemcategory, purpose=purpose, status=status,
                                        problemSize=problemsize, organization=organization)

        if request.FILES:
            post_data.image = request.FILES.get('image')

        return render(request, 'app/index.html', {
            'post_data': post_data, 'form': form
        })


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


class Calory(View):
    def inucalory(request, *args, **kwargs):

        return render(request, 'app/inu_calory.html')

    def nekocalory(request, *args, **kwargs):

        return render(request, 'app/neko_calory.html')

    def calory_form(request):

        weight = float(request.POST['weight'])

        # RER:安静時エネルギー要求量計算
        def RER(weight):
            f = weight ** 3
            first_sqrt = math.sqrt(f)
            # print(first_sqrt)
            second_sqrt = math.sqrt(first_sqrt)
            # print(second_sqrt)
            rer = int(second_sqrt * 70)
            return rer

        # DER:1日あたりのエネルギー要求量
        def DER(rer):
            while True:
                q1 = int(request.POST['inuneko'])
                # 計算したいのが犬ならば
                if q1 == 1:
                    while True:
                        dog_q1 = int(request.POST['select'])

                        # 成犬ならば
                        if dog_q1 == 1:
                            dog_q2 = int(request.POST['q1'])
                            if dog_q2 == 1:
                                der = int(rer * 1.6)
                                return der

                            elif dog_q2 == 2:
                                der = int(rer * 1.8)
                                return der

                            else:
                                print("1または2を入力")
                                continue

                        # 子犬ならば
                        elif dog_q1 == 2:
                            while True:
                                born = int(request.POST['q2'])
                                if born < 4:
                                    der = int(rer * 3.0)
                                    return der
                                elif born >= 4 and born <= 9:
                                    der = int(rer * 2.5)
                                    return der
                                elif born >= 10 and born <= 12:
                                    der = int(rer * 2.0)
                                    return der
                                else:
                                    print("12以内で入力")
                                    continue

                        # 高齢犬または肥満傾向ならば
                        elif dog_q1 == 3:
                            der = int(rer * 1.4)
                            return der

                        # 入力エラーならば
                        else:
                            print("1、2、3のどれかを入力")
                            continue

                # 猫の場合
                elif q1 == 2:
                    while True:
                        cat_q1 = int(request.POST['select'])

                        # 成猫の場合
                        if cat_q1 == 1:
                            cat_q2 = int(request.POST['q1'])

                            if cat_q2 == 1:
                                der = int(rer * 1.2)
                                return der

                            elif cat_q2 == 2:
                                der = int(rer * 1.4)
                                return der

                            else:
                                print("1または2を入力")
                                continue

                        # 子猫の場合
                        elif cat_q1 == 2:
                            while True:
                                born = int(request.POST['q2'])
                                if born < 4:
                                    der = int(rer * 3.0)
                                    return der
                                elif born >= 4 and born <= 6:
                                    der = int(rer * 2.5)
                                    return der
                                elif born >= 7 and born <= 12:
                                    der = int(rer * 2.0)
                                    return der
                                else:
                                    print("12以内で入力")
                                    continue

                        # 高齢の場合
                        elif cat_q1 == 3:
                            der = int(rer * 1.1)
                            return der

                        # デブ猫なら
                        elif cat_q1 == 4:
                            der = int(rer * 1.0)
                            return der

                        # 入力エラーの場合
                        else:
                            print("1、2、3のどれかを入力")
                            continue

                # 入力エラーの場合
                else:
                    print("1または2で入力 犬猫")
                    continue

        # 一日の必要なカロリーを計算
        def FOOD(der):
            g_kcal = int(request.POST['calory'])
            one_kcal = float(g_kcal / 100)
            food = int(der / one_kcal)
            return food

        rer = RER(weight)
        der = DER(rer)
        food = FOOD(der)

        print("約" + str(food) + "g")

        return render(request, 'app/calory.html', {'food': food

                                                   })

class BCS(View):
    def inuBCS(request, *args, **kwargs):

        return render(request, 'app/inu_bcs.html')

    def nekoBCS(request, *args, **kwargs):

        return render(request, 'app/neko_bcs.html')

    def bcs_form(request):





        bcs=0

        return render(request, 'app/Bcs.html', {'bcs': bcs

                                                   })
