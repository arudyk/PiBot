from django.conf.urls import patterns, url                                      
                                                                                
from virt_tours import views                                                
                                                                                
urlpatterns = patterns('',                                                      
    url(r'^$', views.index, name='index'),                                      
    url(r'^register/$', views.register, name='register'),                       
    url(r'^login/$', views.login, name='login'),                                
                                                                                
    # User auth urls                                                            
    url(r'^login/$', 'virt_tours.views.login'),                             
    url(r'^auth/$', 'virt_tours.views.auth_view'),                          
    url(r'^logout/$', 'virt_tours.views.logout'),                           
    url(r'^loggedin/$', 'virt_tours.views.loggedin'),                       
    url(r'^invalid/$', 'virt_tours.views.invalid_login'),                   
)                                                                               
                  
