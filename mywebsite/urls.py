"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

# http://127.0.0.2:8080/
    url(r"^$",views.index,name='home'),

# http://127.0.0.2:8080/
    url(r"^",include("myuser.urls")),


# http://127.0.0.2:8080/home/
    url(r"^home/$",views.home),

# http://127.0.0.2:8080/blog/ => mywebsite_blog
    url(r"^blogs/", include('blog.urls',namespace="blog"),name="mywebsite_blog"),
    # url(r"^blog/$", include('blog.urls'))

# http://127.0.0.2:8080/movies/
    url(r"^movies/", include('movie.urls'))
    # url(r"^blog/$", include('blog.urls'))
]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)