from django.conf.urls import patterns, url

from virt_tours import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # user auth urls
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid_login, name='invalid_login'),
)

