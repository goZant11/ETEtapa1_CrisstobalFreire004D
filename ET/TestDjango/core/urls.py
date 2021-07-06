from django.urls import path
from .views import Ver, form_colab, form_del_colab, form_mod_colab, home

urlpatterns = [
    path('',home,name="home"),
    path('form_colab',form_colab,name="form_colab"),
    path('ver', Ver, name='ver'),
    path('form_mod_colab/<id>', form_mod_colab, name="form_mod_colab"),
    path('form_del_colab/<id>',form_del_colab, name="form_del_colab"),
]
