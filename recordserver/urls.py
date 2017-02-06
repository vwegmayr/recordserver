from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView
from django import get_version
from sumatra_server import __version__ as ss_version
from sumatra import __version__ as smt_version
admin.autodiscover()


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['version'] = {"Django": get_version(), "sumatra-server": ss_version, "Sumatra": smt_version}
        return context


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
    url(r'^accounts/change_password/$', 'django.contrib.auth.views.password_change', {"post_change_redirect": settings.LOGIN_REDIRECT_URL}, name="change_password"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^about/$', AboutView.as_view(), name="about"),
    (r'^records/', include('sumatra_server.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
