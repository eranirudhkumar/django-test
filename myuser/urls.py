from django.conf.urls import url

from . import views

urlpatterns = [

    # http://127.0.0.1:8000/login/
    url(r"^login/$", views.login1, name='user-login'),

    # http://127.0.0.1:8000/register/
    url(r"^register/$", views.register, name='user-register')
]
