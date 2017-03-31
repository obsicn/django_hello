
from django.conf.urls import url
from hello_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]