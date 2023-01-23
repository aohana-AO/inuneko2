from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('inu_random', views.APItati.inu, name='inu_random'),
    path('CaloryInu', views.Calory.inucalory, name='CaloryInu'),
    path('CaloryNeko', views.Calory.nekocalory, name='CaloryNeko'),
    path('inuBCS', views.BCS.inuBCS, name='inuBCS'),
    path('nekoBCS', views.BCS.nekoBCS, name='nekoBCS'),
    path('BCS', views.BCS.bcs_form, name='BCS'),
    path('Calory_form', views.Calory.calory_form, name='Calory_form'),
    path('sibainu_random', views.APItati.sibainu, name='sibainu_random'),
    path('post_create', views.CreatePost.as_view(), name='post_create'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>delete/',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>edit/',views.PostEditView.as_view(),name='post_edit'),
]