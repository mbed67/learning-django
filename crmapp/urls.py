from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage

admin.autodiscover()

urlpatterns = patterns('',
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name='sub_new'),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),

    # Account related URLs

    # Contact related URLS

    # Communication related URLs

)
