from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage

urlpatterns = patterns('',
    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs

    # Account related URLs

    # Contact related URLS

    # Communication related URLs

)
