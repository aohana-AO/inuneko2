from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inu_random', views.APItati.inu, name='inu_random'),
    path('Calory', views.Calory.calory, name='Calory'),
    path('Calory_form', views.Calory.calory_form, name='Calory_form'),
    path('sibainu_random', views.APItati.sibainu, name='sibainu_random'),
    path('post_create', views.CreatePost.as_view(), name='post_create'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>delete/',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>edit/',views.PostEditView.as_view(),name='post_edit'),
]