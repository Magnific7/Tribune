from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views 
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('news.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^accounts/login/$', views.login)
    # url(r'^accounts/profile/',
    #      TemplateView.as_view(template_name='accounts/profile.html'),
    #      name='profile'),

]    # url(r'^accounts/login/$',
    # auth_views.login, 
    # {'template_name': 'profile.html'}, 
    # name='login'