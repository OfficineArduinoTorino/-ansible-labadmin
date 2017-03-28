from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


labadminpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^labAdmin/', include('labAdmin.urls')),

    url(r'^accounts/login/$', auth_views.login, {'template_name': 'labadmin/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^$', TemplateView.as_view(template_name='labadmin/index.html')),
]

urlpatterns = [
    url(r'^labadmin/', include(labadminpatterns)),
]
