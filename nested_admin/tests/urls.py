import django
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin

# Explicitly import to register the admins for the test models
for app in settings.INSTALLED_APPS:
    if app.startswith('nested_admin.tests.'):
        __import__("%s.admin" % app)


urlpatterns = [
    re_path(r'^_nesting/', include('nested_admin.urls')),
]

urlpatterns += [re_path(r'^admin/', admin.site.urls)]

try:
    import grappelli
except ImportError:
    pass
else:
    urlpatterns += [re_path(r"^grappelli/", include("grappelli.urls"))]
