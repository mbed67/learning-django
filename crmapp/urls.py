from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage
from accounts.views import AccountList
from accounts.urls import account_urls
from contact.urls import contact_urls

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
    url(r'^account/news/$', 'crmapp.accounts.views.account_cru', name='account_new'),
    url(r'^account/list/$', AccountList.as_view(), name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),

    # Contact related URLS
    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),

    # Communication related URLs

)
