from django.conf.urls import url
from . import views

urlpatterns = [

# http://127.0.0.2:8080/blog/
    url(r"^$", views.blog_index),



# http://127.0.0.2:8080/blog/user/new_user/  =>blog_user_signup
    url(r"^user/new_user/$", views.new_user,name="blog_user_signup"),

# http://127.0.0.2:8080/blog/user/login/ =>blog_user_login
    url(r"^user/login/$", views.user_login,name="blog_user_login"),




# http://127.0.0.2:8080/blog/user/form/login/
    url(r"^user/form/login/$", views.user_form_login),



# http://127.0.0.2:8080/blog/user_register/
    url(r"^user_register/$", views.user_register),


# http://127.0.0.2:8080/blog/user_register/
    url(r"^bootstrap/$", views.bootstrap),


# http://127.0.0.2:8080/blog/student-list/
    url(r"^student-list/$", views.student_list),





]