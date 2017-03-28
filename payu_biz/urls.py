from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^payubiz-success/$','payu_biz.views.payu_success', name='payu_success'),

    url(r'^payubiz-failure/$', 'payu_biz.home.views.payu_failure', name='payu_failure'),
 
    url(r'^payubiz-cancel/$', 'payu_biz.views.payu_cancel', name='payu_cancel'),

)
