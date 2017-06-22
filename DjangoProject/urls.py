from django.conf.urls import *
from django.contrib import admin
from DjangoProject1.views import hello
# from django.views import *DjangoProject/urls.py:3
# from myapp import views as myapp_views
# from myapp.views import home, contact
# from django.contrib.auth import views as auth_views
# from myapp import views as myapp_views

admin.autodiscover()

urlpatterns = [
   #Examples
   #url(r'^$', 'myproject.view.home', name = 'home'),
   #url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
   # url(r'^hello/', 'DjangoProject1.views.hello', name = 'hello'),
   url(r'^hello/$', hello),
   # views.hello, name='hello'),
]